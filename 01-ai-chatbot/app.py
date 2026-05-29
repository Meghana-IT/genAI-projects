import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()

client = Groq(


    
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot - Custom Assistant")
st.write("Ask me anything. I can act like a tutor, friend, or coding assistant.")

# Sidebar
st.sidebar.title("⚙️ Settings")

assistant_type = st.sidebar.selectbox(
    "Choose Assistant Type",
    ["Tutor", "Friend", "Coding Assistant"]
)

if assistant_type == "Tutor":
    system_prompt = "You are a helpful tutor. Explain concepts in simple beginner-friendly language."
elif assistant_type == "Friend":
    system_prompt = "You are a friendly assistant. Reply casually and supportively."
else:
    system_prompt = "You are a coding assistant. Explain code, fix errors, and give examples."

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# Reset chat
if st.sidebar.button("Reset Chat"):
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]
    st.rerun()

# Display old messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages,
                temperature=0.7
            )

            bot_reply = response.choices[0].message.content
            st.write(bot_reply)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )