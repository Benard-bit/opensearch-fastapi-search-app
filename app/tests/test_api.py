import pytest
import httpx
from fastapi.testclient import TestClient
from ..main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "Поиск по документам" in response.text


def test_search_for_word():
    response = client.get("/?q=Docker")
    assert response.status_code == 200
    assert "A Guide to Docker" in response.text
    assert "Python for Data Science" not in response.text


def test_search_with_filter():
    response = client.get("/?q=guide&content_type=book")
    assert response.status_code == 200
    assert "A Guide to Docker" not in response.text
    assert "Introduction to OpenSearch" not in response.text

    response = client.get("/?q=guide&content_type=guide")
    assert response.status_code == 200
    assert "A Guide to Docker" in response.text
    assert "Introduction to OpenSearch" in response.text


def test_search_empty_query():
    response = client.get("/?q=")
    assert response.status_code == 200
    assert "Результаты поиска:" not in response.text


def test_search_no_results():
    response = client.get("/?q=abracadabraxyz")
    assert response.status_code == 200
    assert "Ничего не найдено по запросу" in response.text
