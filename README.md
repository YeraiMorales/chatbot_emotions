
# 🤖 EmotionBot: Emotion Analysis Chatbot

A Full-Stack AI Chatbot that detects the user's emotions and responds empathetically. 

Built with **FastAPI** (Backend), **Streamlit** (Frontend), and **PyTorch** based **Hugging Face Transformers** (NLP Model).

## Features
- **Emotion Detection:** Uses a pre-trained RoBERTa model (`j-hartmann/emotion-english-distilroberta-base`) to classify text into emotions like Joy, Anger, Sadness, Fear, Surprise, and Neutral.
- **Empathetic Responses:** The bot adapts its personality and responses based on the detected emotion.
- **Microservices Architecture:** Decoupled architecture with a REST API backend and a separate frontend interface.

## Tech Stack
- **Python 3.9+**
- **FastAPI**: High-performance backend API.
- **Streamlit**: Interactive web interface.
- **Transformers (Hugging Face)**: NLP Pipeline.
- **Torch**: Machine Learning backend (CPU optimized).

## Installation

1. **Clone the repository:**
```bash
git clone [https://github.com/YeraiMorales/chatbot_emotions.git](https://github.com/YeraiMorales/chatbot_emotions.git)
cd chatbot_emotions
```


2. **Create a virtual environment:**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```


3. **Install dependencies:**
```bash
pip install -r requirements.txt
```



## Usage

You need to run the Backend and the Frontend in two separate terminals.

**Terminal 1: Start the API**

```bash
uvicorn api:app --reload
```

*The API will start at http://127.0.0.1:8000/*

**Terminal 2: Start the Chatbot Interface**

```bash
streamlit run frontend.py
```

*The web app will open automatically in your browser (usually http://localhost:8501).*

## 📂 Project Structure

```
├── api.py           # FastAPI backend & Model inference
├── frontend.py      # Streamlit web interface
├── requirements.txt # Project dependencies
├── README.md        # Project documentation
└── .gitignore       # Ignored files
```