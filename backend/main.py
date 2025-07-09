from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from random import random

app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    emotion: str
    confidence: float

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_emotion(request: AnalyzeRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text is required.")
    # Mock emotion analysis
    emotions = ["Happy", "Sad", "Angry", "Anxious", "Excited", "Calm"]
    import random
    emotion = random.choice(emotions)
    confidence = round(random.uniform(0.7, 0.99), 2)
    return {"emotion": emotion, "confidence": confidence} 