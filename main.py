from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from functools import lru_cache
from transformers import pipeline

class TextInput(BaseModel):
    text: str

class SentimentOutput(BaseModel):
    label: str
    score: float

@lru_cache(maxsize=1)
def get_sa():
    return pipeline("sentiment-analysis")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ok"}

@app.post("/predict-sentiment", response_model=SentimentOutput)
async def predict_sentiment(input: TextInput):
    try:
        s = get_sa()(input.text)[0]
        return {"label": s["label"], "score": s["score"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
