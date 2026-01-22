import streamlit as st
import requests
import random

# Page config
st.set_page_config(page_title="EmotionBot", page_icon="🤖")

st.title("🤖 EmotionBot: The Empathetic Chatbot")
st.write("Tell me how you feel, and I'll react to your emotions.")

# API URL
API_URL = "http://127.0.0.1:8000/analyze"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Dictionary with multiple responses per emotion
responses = {
    "joy": [
        "That sounds amazing! I'm so happy for you! 🎉",
        "Awesome! Keep up the great vibes!",
        "Hearing that makes my digital heart smile! 😄",
        "Fantastic news! Tell me more!"
    ],
    "anger": [
        "I can sense your frustration. Take a deep breath. 🧘",
        "I understand why you are upset. I'm here to listen.",
        "It's okay to be angry sometimes. Let it out.",
        "That sounds really annoying. I'm on your side."
    ],
    "sadness": [
        "I'm so sorry you're feeling this way. 💙",
        "Sending you a virtual hug. You are not alone.",
        "That sounds tough. Do you want to talk about it?",
        "I wish I could do more than just process text to help you."
    ],
    "fear": [
        "It's natural to be scared. You can get through this.",
        "Take it one step at a time. Everything will be okay.",
        "Fear is just a reaction. You are stronger than you think.",
        "I'm here with you. Don't worry."
    ],
    "surprise": [
        "Wow! I didn't see that coming! 😲",
        "Really? That is unexpected!",
        "No way! Tell me more details!",
        "You've definitely surprised me with that one."
    ],
    "neutral": [
        "Got it. Thanks for sharing.",
        "I see. Anything else on your mind?",
        "Understood. I'm listening.",
        "Okay, cool."
    ]
}

def get_bot_response(emotion, confidence):
    # Select a random list of phrases based on the emotion
    # If the emotion is not in our dict, default to "neutral"
    phrases = responses.get(emotion, responses["neutral"])
    
    # Pick one random phrase
    selected_phrase = random.choice(phrases)
    
    # Confidence score for debugging/info
    return f"{selected_phrase}" # (Confidence: {confidence:.2f})"

# Capture user input
if prompt := st.chat_input("How are you feeling today?"):
    # Save and display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call API
    with st.chat_message("assistant"):
        with st.spinner("Analyzing vibes..."):
            try:
                response_api = requests.post(API_URL, json={"text": prompt})
                
                if response_api.status_code == 200:
                    data = response_api.json()
                    emotion = data["emotion"]
                    confidence = data["confidence"]
                    
                    # Generate random response
                    bot_reply = get_bot_response(emotion, confidence)
                    
                    st.markdown(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                else:
                    st.error("Error connecting to the bot's brain.")
            except Exception as e:
                st.error(f"Connection failed. Is the API running? Error: {e}")