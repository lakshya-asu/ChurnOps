# ChurnOps: An End-to-End MLOps Pipeline for Customer Churn Prediction

ChurnOps is an end-to-end MLOps pipeline project designed to predict customer churn using robust MLOps practices. This project demonstrates the entire machine learning lifecycle—from data ingestion and model training to deployment and continuous integration—showcasing best practices in MLOps.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Data Preparation](#data-preparation)
- [Usage](#usage)
  - [Model Training](#model-training)
  - [Running the API](#running-the-api)
  - [Containerization with Docker](#containerization-with-docker)
  - [CI/CD with GitHub Actions](#cicd-with-github-actions)

## Overview

ChurnOps is built to predict customer churn and demonstrates a full MLOps pipeline including:
- **Data Ingestion & Preprocessing:** Automates data loading, cleaning, and splitting.
- **Experiment Tracking:** Uses MLflow to log experiments and track model performance.
- **Model Training:** Implements a logistic regression model for churn prediction.
- **REST API Deployment:** Exposes a Flask API for real-time predictions.
- **Containerization:** Uses Docker to containerize the application.
- **CI/CD Pipeline:** Implements GitHub Actions to automate testing and Docker builds.

## Features

- **End-to-End Pipeline:** Covers the complete machine learning lifecycle.
- **Data Ingestion:** Loads and preprocesses raw data, splitting it into training and test sets.
- **Experiment Tracking:** Logs experiments, metrics, and models with MLflow.
- **API Deployment:** Provides a RESTful API for serving model predictions.
- **Containerization:** Simplifies deployment using Docker.
- **CI/CD Integration:** Ensures quality and automated deployment with GitHub Actions.

## Project Structure
```console
ChurnOps/ 
├── data/ 
│ └── churn.csv # Your raw churn data (CSV format) 
├── model/ 
│ └── churn_model.pkl # Trained model (generated after training) 
├── src/ 
│ ├── data_ingestion.py # Script for loading and splitting data 
│ ├── train.py # Model training script with MLflow tracking 
│ └── app.py # Flask API to serve predictions 
├── Dockerfile # Containerization for the API 
├── requirements.txt # Python dependencies 
└── .github/ └── workflows/ 
└── ci.yml # GitHub Actions CI/CD pipeline configuration
```


## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Docker (for containerization)
- A GitHub account

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/ChurnOps.git
   cd ChurnOps


2. Create a Virtual Environment (Optional but Recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install Python Dependencies
    ```bash
    pip install -r requirements.txt


Data Preparation
- Place your raw churn data file (churn.csv) in the data/ directory.
- Run the data ingestion script to load, clean, and split the data:
    ```bash
        python src/data_ingestion.py

### Usage
#### Model Training
Train the churn prediction model and log the experiment with MLflow:
    ```bash
        python src/train.py


The API provides:
- POST /predict: Accepts a JSON payload with a "features" key containing the input data.
- GET /health: Returns a health check status.
#### Containerization with Docker
    1. Build the Docker Image:
        ```bash
            docker build -t churnops:latest .
    2. Run the Docker Container:
        ```bash
           docker run -p 5000:5000 churnops:latest
 
The API will be accessible at `http://localhost:5000`.

### CI/CD with GitHub Actions
A GitHub Actions workflow is set up in `.github/workflows/ci.yml` to automate:

- Checking out the code
- Installing dependencies
- Running basic tests (e.g., module import tests)
- Building the Docker image
This workflow triggers on pushes and pull requests to the `main` branch.