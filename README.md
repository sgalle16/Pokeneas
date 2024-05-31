# Pokeneas App
This project is a version of a Pokedex application built with Flask named Pokeneas, deployed as a microservice using Docker Swarm on Google Cloud Platform (GCP). The application showcases the capabilities of containerization and orchestration by providing a scalable and easily deployable solution for serving random Pokemon-like data called pokeneas.

## Description
The application displays random information about different Pokeneas. It has two main routes:
### Routes
- `/api/pokenea`: Returns a JSON with information about a random Pokenea.
- `/pokenea`: Displays an HTML page with the image and an antioqueña philosophical phrase of a random Pokenea.

## Features
- **Flask**: A simple web application that returns a random Pokenea information.
- **Docker**: Containerized Flask application for easy deployment and scaling.
- **Docker Swarm**: Utilizes Docker Swarm for deploying and managing multiple instances of the service.
- **Google Cloud Platform (GCP)**: Cloud platform for deploying VM instances and managing the Docker Swarm cluster.
- **Google Cloud Storage**: Service for storing Pokemon images.
- **GitHub Actions**: For continuous integration and automated Docker image deployment.
- **DockerHub**: Repository for storing Docker images.

## Running the App with Docker

### Option 1: Use Existing Docker Image

1. **Pull and run the Docker image from DockerHub:**:
    ```bash
    docker pull sgalle16/flask-pokeneas:latest
    docker run -p 5000:80 sgalle16/flask-pokeneas:latest
    ```
### Option 2: Build Your Own Docker Image

2. **Build and run your own Docker image:**:
    ```bash
    docker build -t <YOUR_DOCKERHUB_USERNAME>/pokeneas:latest .
    docker run -p 5000:80 <YOUR_DOCKERHUB_USERNAME>/pokeneas:latest
    ```

### Access the application:
  - JSON route: [http://localhost:5000/api/pokenea](http://localhost:5000/api/pokenea)
  - HTML route: [http://localhost:5000/pokenea](http://localhost:5000/pokenea)

