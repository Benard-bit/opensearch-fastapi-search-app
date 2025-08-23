# Search service on FastAPI and OpenSearch

<p align="center"> 
<img src="https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9"/> 
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/> 
<img src="https://img.shields.io/badge/OpenSearch-005EB8?style=for-the-badge&logo=opensearch&logoColor=white" alt="OpenSearch"/> 
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
<img src="https://img.shields.io/badge/Pytest-0A9B71?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest"/>
</p>

This is a full-featured web application that implements a search service with filtering by content type. The project is fully containerized using Docker, which ensures fast startup and identical environment. The quality of the code is confirmed by integration tests.

## 🚀 Key features

- **Full-text search**: Search by keyword in the title (`title`) and content (`content`) of documents.
- **Filtering**: Ability to filter search results by content type (`article`, `guide`, `book`, `news`).
- **Ready-to-use infrastructure**: Launch the entire stack (OpenSearch + web application) with a single command via `docker-compose`.
- **Automatic filling**: At the first launch, the database is automatically created and filled with test data.
- **Autotests**: The quality and correctness of the API are confirmed by a set of integration tests (`pytest`).
- **Fault-tolerant launch**: Thanks to `healthcheck`, the web application starts only after OpenSearch is fully ready to accept connections.

---

## ⚙️ Step-by-step project launch

To launch the project, you will need **Git** and **Docker** (with Docker Compose) installed.

### Step 1: Clone the repository

Open a terminal and run the following command to copy the project to your computer.

```bash
git https://github.com/averageencoreenjoer/opensearch-fastapi-search-app.git
cd opensearch-fastapi-search-app
```

### Step 2: Create a config file

The project uses environment variables for configuration. Copy the example file to create your working config file.

```bash
cp .env.example .env
```
*No changes are required inside the file, as all settings are already optimized for Docker.*

### Step 3: Build and run containers

Run a single command that will download the images, build the web app container, and start all services in the background.

```bash
docker-compose up --build -d
```
- `--build`: Forces a rebuild of your application image if there have been changes in the code.
- `-d`: Starts containers in the background (detached mode).

> **Please wait:** OpenSearch may take about 30-60 seconds to fully initialize. The web app will start automatically once the database is ready.

### Step 4: Check if it works

Open your web browser and go to:

**[http://localhost:8000](http://localhost:8000)**

You should see the web interface of the search service. Try searching for `Python`, `Docker` or `software` and apply different filters.

---

## ✅ Run automated tests

The project is covered with integration tests that check if the search and filter APIs work correctly.

To run the tests, run the following command in the terminal:

```bash
docker-compose exec webapp python -m pytest
```

#### Expected result:
You will see a report of **5 successfully passed tests** without errors or warnings.
```
= ... ├── app/ # Directory with application code
│ ├── main.py # Main FastAPI file (endpoints, launch)
│ ├── opensearch_client.py # Module for all logic of working with OpenSearch
│ ├── requirements.txt # Python dependencies
│ ├── templates/ # HTML templates
│ │ └── index.html
│ └── tests/ # Integration tests
│ └── test_api.py
├── .gitignore # File for excluding garbage files from Git
├── docker-compose.yml # File for orchestration Docker containers
├── Dockerfile # Instructions for building a web application image
├── .env.example # Example file with environment variables
└── README.md # This file
```

---

## 🛑 Stopping the application

To stop and remove all running containers, run the command:

```bash
docker-compose down
```
This command will also remove the created Docker network, but will not affect OpenSearch data thanks to `volume`.