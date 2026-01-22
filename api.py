from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI(title="Emotion Analysis API", version="1.0")

# Load the pre-trained model for emotion classification
print("Loading AI model...")
emotion_classifier = pipeline(
    "text-classification", 
    model="j-hartmann/emotion-english-distilroberta-base", 
    device=-1  # IMPORTANT: Force CPU usage
)

# Define the format of the data we expect to receive
# Pydantic takes care of validating that we receive a correct text.
class UserText(BaseModel):
    text: str

# Create the endpoint
# When someone sends data to /analyze, this function is executed.
@app.post("/analyze")
def analyze_emotion(input: UserText):
    # Use the model
    result = emotion_classifier(input.text)
    
    # Extract clean information
    emotion = result[0]['label']
    confidence = result[0]['score']
    
    # Return a JSON (dictionary)
    return {
        "emotion": emotion, 
        "confidence": confidence, 
        "original_text": input.text
    }

# Test endpoint to check if the API is alive
@app.get("/")
def home():
    return {"message": "The emotion API is working correctly"}