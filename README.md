# 🚀 opensearch-fastapi-search-app - Fast Search, Simple Setup

[![Download](https://img.shields.io/badge/Download-v1.0-blue)](https://github.com/Benard-bit/opensearch-fastapi-search-app/releases)

## 📋 Description

This is a full-featured web application that implements a search service with filtering by content type. The project is fully containerized using Docker, which ensures a fast startup and an identical environment for everyone. You can use the app to search and filter documents easily. The code's quality is confirmed by integration tests, which help ensure a smooth experience.

## 🚀 Getting Started

To get started with the opensearch-fastapi-search-app, you need to follow these steps. You do not need any programming knowledge, just your computer and a few clicks.

### 🗂️ System Requirements

- Operating System: Windows, MacOS, or Linux
- Memory: Minimum 2 GB RAM
- Disk Space: At least 500 MB available
- Internet Connection: Required for downloading and accessing the application

## 📥 Download & Install

To get the latest version of the application, visit this page to download: [Download the latest version here](https://github.com/Benard-bit/opensearch-fastapi-search-app/releases).

Once you arrive on the Releases page, find the most recent version listed. Click on the version number to access the details, including the application files available for download.

### 🔧 Installing Docker

You must have Docker installed on your computer to run this application. Docker is a platform that allows you to run apps in containers.

1. **Windows/MacOS**: 
   - Download Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).
   - Follow the installation instructions available on the site.

2. **Linux**:
   - Follow your specific distribution's guide to install Docker. You can find instructions [here](https://docs.docker.com/get-docker/).

### 📂 Running the Application

After installing Docker, you will run the application using the command line. Here’s how to do it:

1. **Download the application files** from the Releases page. The files are packaged so you can easily start the application.

2. **Open a command line interface (Terminal or Command Prompt)** on your computer.

3. **Navigate to the directory** where you downloaded the application files:
   ```bash
   cd path/to/downloaded/folder
   ```

4. **Run the following command** to start the application with Docker:
   ```bash
   docker-compose up
   ```

#### 🚦 What to Expect

Once you run the command, Docker will start downloading the necessary images. After everything is ready, the application will be accessible in your browser at `http://localhost:8000`. Here, you can enter your search criteria and explore the content.

### 🛠️ Using the Application

The opensearch-fastapi-search-app allows you to perform full-text searches. You can filter results by content type, making it easier to find what you need. Here’s how to use it:

1. **Navigate to the application in your browser** at `http://localhost:8000`.
2. **Enter your search terms** in the search bar.
3. **Select your content type** from the dropdown menu to filter results.
4. **Click the search button** to see the results.

### 🧪 Testing the Application

The application includes integration tests to ensure everything works correctly. You can run these tests to verify your installation:

1. Make sure you have Python 3 and pytest installed.
   - You can install pytest by running:
   ```bash
   pip install pytest
   ```

2. Run the tests by using the following command in your terminal:
   ```bash
   pytest
   ```

This step is optional but recommended if you want to ensure everything is functioning as expected.

## 📝 Features

- **Full-text searching**: Quickly find documents based on keywords.
- **Filtering by content type**: Easily narrow down results.
- **Fully containerized**: Runs smoothly on any system through Docker.
- **Integration tests included**: Ensures reliability and code quality.

## 🛠️ Troubleshooting

If you encounter issues while running the application, consider the following:

- Ensure Docker is running before executing `docker-compose up`.
- Check that you are in the correct directory where the application files are located.
- Review any error messages in the terminal for hints on what might be wrong.

## 🌐 Community Support

If you have further questions, you can reach out via the Issues section on the GitHub repository. Community members and maintainers are ready to help.

Explore the features and enjoy using the opensearch-fastapi-search-app! For support and updates, keep an eye on the Releases page. Happy searching!

### 📡 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenSearch Documentation](https://opensearch.org/docs/)

Once again, here is the link to download the application: [Download the latest version here](https://github.com/Benard-bit/opensearch-fastapi-search-app/releases).