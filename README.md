# Intelligent Book Management System

This project is an intelligent book management system built using Python, FastAPI, PostgreSQL, and a locally running Llama3 generative AI model. The system allows users to add, retrieve, update, and delete books from a PostgreSQL database, generate summaries for books using the Llama3 model, and provide book recommendations based on user preferences. Additionally, it manages user reviews and generates rating summaries for books. The application is designed to be accessible via a RESTful API and deployed on the cloud (AWS).

## Features
- Add, update, delete, and retrieve books.
- Add, retrieve, and aggregate reviews for books.
- Generate book and review summaries using Llama3.
- Provide book recommendations based on user preferences.
- Asynchronous operations for database interactions and AI model predictions.
- RESTful API with Swagger documentation.
- Basic authentication for API endpoints.
- Cloud deployment using AWS services.

## Table of Contents
- [Technologies](#technologies)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
- [Setup Instructions](#setup-instructions)
- [Running Locally](#running-locally)
- [Cloud Deployment (AWS)](#cloud-deployment-aws)
- [Testing](#testing)
- [Bonus Features](#bonus-features)

## Technologies
- **Backend**: FastAPI, Python 3.10+
- **Database**: PostgreSQL
- **AI Model**: Llama3 (Locally running or via Hugging Face)
- **Asynchronous Programming**: SQLAlchemy [asyncio], asyncpg
- **Cloud**: AWS EC2, RDS, S3, ElastiCache (Optional), SageMaker (Optional)
- **Authentication**: JWT Tokens (FastAPI Security)
- **Deployment**: Docker, AWS EC2, AWS Lambda, GitHub Actions CI/CD

## Database Schema
### Books Table
```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    year_published INT,
    summary TEXT
);


### Explanation of the README Sections:
- **Technologies**: A list of technologies and tools used.
- **Database Schema**: SQL for creating tables in PostgreSQL.
- **API Endpoints**: All the available API endpoints for interacting with the system.
- **Setup Instructions**: Step-by-step guide to set up the project locally.
- **Running Locally**: Instructions for starting the application locally.
- **Cloud Deployment**: Instructions for deploying the application on AWS.
- **Testing**: Instructions for running unit tests using `pytest`.
- **Bonus Features**: Additional features such as caching and using AWS SageMaker for ML models.

This README should help users set up, run, and deploy the intelligent book management system.
