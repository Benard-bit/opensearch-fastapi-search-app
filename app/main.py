from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import opensearch_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    opensearch_client.get_opensearch_client()
    opensearch_client.create_index_if_not_exists()
    yield

app = FastAPI(title="Senior OpenSearch Demo", lifespan=lifespan)


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def search_page(request: Request, q: str = None, content_type: str = "all"):
    results = []
    if q:
        results = opensearch_client.search_documents(query=q, content_type=content_type)

    context = {
        "request": request,
        "results": results,
        "query": q,
        "selected_content_type": content_type
    }
    return templates.TemplateResponse(request, "index.html", context)
