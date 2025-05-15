from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="Sentiment Checker API")

class Message(BaseModel):
    text: str

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/analyze")
def analyze_sentiment(message: Message):
    if "good" in message.text.lower():
        sentiment = "positive"
    elif "bad" in message.text.lower():
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return {"sentiment": sentiment}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
