import streamlit as st
import random

# --- PAGE SETUP ---
st.set_page_config(page_title="Climate Health AI Chatbot 🌍", page_icon="🤖", layout="centered")

st.title("🤖 Climate Health AI Chatbot")
st.markdown("### Learn how climate change impacts our health — ask me anything!")

# --- RESPONSE DATABASE ---
responses = {
    "greeting": [
        "Hi there! 🌞 I’m your Climate Health Bot. How can I help you today?",
        "Hello! I'm here to talk about how climate change affects our health. Ask me anything!"
    ],
    "air_quality": [
        "Air pollution causes asthma, heart disease, and even lung cancer. Try planting trees and using public transport more often.",
        "Poor air quality increases respiratory problems. Masks on smoggy days help protect your lungs."
    ],
    "heat": [
        "Rising temperatures can cause heat strokes and dehydration. Stay hydrated and avoid long sun exposure.",
        "Extreme heat waves can be dangerous. Always wear light clothing and drink plenty of water!"
    ],
    "water": [
        "Climate change affects water quality — floods and droughts can spread waterborne diseases.",
        "Unsafe water may carry cholera and typhoid. Always boil or filter drinking water in risky areas."
    ],
    "food": [
        "Climate change affects crops, leading to food insecurity and malnutrition in many regions.",
        "Extreme weather affects farming — eat local and reduce food waste to help the planet!"
    ],
    "mental_health": [
        "Climate anxiety is real. Talk about your feelings and take small eco-friendly steps to feel empowered.",
        "Extreme weather disasters cause stress. Protect your mental health and support your community!"
    ],
    "default": [
        "That’s interesting! You can ask me about air, heat, water, food, or mental health.",
        "I may not know that yet, but I can tell you how climate change affects our environment and health."
    ]
}


def get_response(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return random.choice(responses["greeting"])
    elif any(word in user_input for word in ["air", "pollution", "smog"]):
        return random.choice(responses["air_quality"])
    elif any(word in user_input for word in ["heat", "hot", "temperature"]):
        return random.choice(responses["heat"])
    elif any(word in user_input for word in ["water", "flood", "drought"]):
        return random.choice(responses["water"])
    elif any(word in user_input for word in ["food", "nutrition", "crop"]):
        return random.choice(responses["food"])
    elif any(word in user_input for word in ["mental", "stress", "anxiety"]):
        return random.choice(responses["mental_health"])
    else:
        return random.choice(responses["default"])


# --- CHAT UI ---
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

user_input = st.chat_input("Ask about climate change & health...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    response = get_response(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
