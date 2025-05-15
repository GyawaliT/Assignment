# Sentiment Checker API (FastAPI)

A simple FastAPI application that returns a basic sentiment ("positive", "negative", "neutral") based on input text.

## Features

- Health check route: `/`
- Sentiment analysis route: `/analyze`

## How to Run

### Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Using Docker

```bash
docker build -t sentiment-api .
docker run -d -p 8000:8000 sentiment-api
```

## Example Usage

POST `/analyze` with JSON:

```json
{
  "text": "This is a good day!"
}
```

Response:

```json
{
  "sentiment": "positive"
}
```
