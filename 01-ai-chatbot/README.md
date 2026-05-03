# 🤖 AI Chatbot - Custom Assistant

## 📌 Objective

The objective of this project is to build a conversational AI chatbot similar to ChatGPT using a simple web interface.
The chatbot interacts with users in real-time and generates intelligent responses using an AI model.

---

## 🚀 Features

* Real-time chat interface
* Maintains conversation history using session state
* Multiple assistant modes:

  * 📘 Tutor (beginner-friendly explanations)
  * 😊 Friend (casual conversation)
  * 💻 Coding Assistant (programming help)
* Reset chat functionality
* Secure API key handling using `.env`

---

## 🛠️ Technologies Used

* Python
* Streamlit (Frontend + Backend)
* Groq API (LLaMA model)
* python-dotenv
* Session State Management

---

## 🔄 Frontend Workflow

1. User opens the Streamlit web application.
2. UI is rendered with:

   * Title and description
   * Sidebar for assistant selection
   * Chat interface
3. User selects assistant type (Tutor / Friend / Coding Assistant).
4. User enters a message using `st.chat_input()`.
5. Message is displayed in chat UI using `st.chat_message()`.

---

## ⚙️ Backend Workflow

1. Application loads environment variables using `dotenv`.

2. Groq client is initialized with API key.

3. Based on selected assistant type, a **system prompt** is created.

4. User input is appended to `session_state.messages`.

5. Entire conversation history (system + user + assistant messages) is prepared.

6. A request is sent to Groq API:

   * Model: `llama-3.1-8b-instant`
   * Messages: conversation history
   * Temperature: controls response randomness

7. Groq API processes input using LLM (Large Language Model).

8. AI-generated response is received.

9. Response is appended to session state.

10. Response is displayed in UI.

---

## 🔁 Data Flow (End-to-End)

User Input → Streamlit UI → Session State → Prompt Construction → Groq API → LLM Processing → Response → UI Display

---

## 🧪 Example Use Cases

* Ask academic doubts
* Get coding explanations
* Practice interview questions
* Casual conversation
* Personal assistant usage

---

## ▶️ How to Run

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Add API Key

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

### Step 3: Run the app

```bash
streamlit run app.py
```

---

## 🔐 Security Note

The `.env` file is excluded using `.gitignore` to protect the API key.
Sensitive data is never uploaded to GitHub.

---

## 📚 What I Learned

* Building interactive web apps using Streamlit
* Integrating AI APIs (Groq)
* Managing state using session state
* Designing system prompts for different assistant behaviors
* Understanding request-response cycle in AI applications
* Secure handling of API keys

---

## 📌 Future Improvements

* Add voice input/output
* Enhance UI/UX design
* Add chat export feature
* Integrate database for persistent storage
* Deploy using Streamlit Cloud / AWS

---

## 📷 Output

A functional chatbot with real-time AI responses and conversation memory.

---

## 👩‍💻 Author

Meghana
