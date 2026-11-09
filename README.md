# SupportOps AI

An end-to-end AI-powered customer support
ticket triage and knowledge assistant.

## Project Objectives

- AI-based ticket classification
- Automated priority prediction
- RAG-based knowledge retrieval
- LLM-powered response suggestions
- ML model versioning using MLflow
- AI evaluation and observability
- Docker containerization
- CI/CD using GitHub Actions
- Cloud deployment using GCP
- Kubernetes orchestration
- Production monitoring

## Technology Stack

Python, FastAPI, Scikit-learn, LangChain,
Chroma, MLflow, RAGAS, Phoenix, Docker,
GitHub Actions, GCP, Kubernetes.

## Current Status

Project initialization.

## Development Setup

Create and activate a virtual environment:

    python3.12 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Run the application:

    uvicorn app.main:app --reload