import os
import time
from opensearchpy import OpenSearch, exceptions
import logging

logging.basicConfig(level=logging.INFO)

HOST = os.getenv("OPENSEARCH_HOST", "localhost")
PORT = int(os.getenv("OPENSEARCH_PORT", 9200))
INDEX_NAME = "content_index"

client = None


def get_opensearch_client():
    global client
    if client is not None:
        return client

    hosts = [{"host": HOST, "port": PORT}]

    for i in range(10):
        try:
            client = OpenSearch(
                hosts=hosts,
                http_auth=("admin", "admin"),
                use_ssl=False,
                verify_certs=False,
                ssl_assert_hostname=False,
                ssl_show_warn=False,
            )
            if client.ping():
                logging.info("Successfully connected to OpenSearch.")
                return client
        except Exception as e:
            logging.warning(f"Connection attempt {i + 1} failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)

    logging.error("Could not connect to OpenSearch after multiple attempts.")
    raise ConnectionError("Failed to connect to OpenSearch.")


def create_index_if_not_exists():
    client = get_opensearch_client()
    if not client.indices.exists(index=INDEX_NAME):
        mappings = {
            "properties": {
                "title": {"type": "text"},
                "content": {"type": "text"},
                "content_type": {"type": "keyword"}
            }
        }
        client.indices.create(index=INDEX_NAME, body={"mappings": mappings})
        logging.info(f"Index '{INDEX_NAME}' created.")
        seed_data()


def seed_data():
    client = get_opensearch_client()
    docs = [
        {"title": "The Art of Programming",
         "content": "An in-depth look at the algorithms and data structures that are the foundation of modern software.",
         "content_type": "article"},
        {"title": "A Guide to Docker",
         "content": "Docker containers wrap up a piece of software in a complete filesystem that contains everything it needs to run.",
         "content_type": "guide"},
        {"title": "Python for Data Science",
         "content": "This book presents a complete guide to using Python for data analysis and scientific computing.",
         "content_type": "book"},
        {"title": "Introduction to OpenSearch",
         "content": "OpenSearch is a powerful open-source search and analytics suite. This guide helps you start.",
         "content_type": "guide"},
        {"title": "Daily Tech News",
         "content": "The latest updates from the world of technology, including software, hardware, and AI.",
         "content_type": "news"}
    ]

    for i, doc in enumerate(docs):
        try:
            client.index(index=INDEX_NAME, body=doc, id=i + 1, refresh=True)
        except exceptions.RequestError as e:
            logging.error(f"Error indexing document {i + 1}: {e}")
    logging.info(f"Seeded {len(docs)} documents.")


def search_documents(query: str, content_type: str = None):
    client = get_opensearch_client()

    search_query = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "content"]
            }
        }
    }

    if content_type and content_type != "all":
        search_query = {
            "query": {
                "bool": {
                    "must": {
                        "multi_match": {
                            "query": query,
                            "fields": ["title", "content"]
                        }
                    },
                    "filter": {
                        "term": {
                            "content_type": content_type
                        }
                    }
                }
            }
        }

    try:
        response = client.search(index=INDEX_NAME, body=search_query)
    except exceptions.NotFoundError:
        logging.warning(f"Index '{INDEX_NAME}' not found during search.")
        return []

    results = []
    for hit in response['hits']['hits']:
        source = hit['_source']
        results.append({
            "title": source['title'],
            "snippet": source['content'][:50] + "..."
        })

    return results
