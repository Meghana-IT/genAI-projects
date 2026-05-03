# ✍️ AI Content Generator

## 📌 Objective

The objective of this project is to build an AI-powered application that generates high-quality content such as blog posts, LinkedIn posts, and Twitter threads based on a given topic.
It helps users quickly create engaging content with different tones and formats.

---

## 🚀 Features

* Topic-based content generation
* Multiple content formats:

  * 📝 Blog Post
  * 💼 LinkedIn Post
  * 🐦 Twitter Thread
* Tone selection:

  * Formal
  * Casual
  * Technical
  * Creative
* Adjustable word limit
* AI-generated structured content
* Simple and interactive UI

---

## 🛠️ Technologies Used

* Python
* Streamlit (Frontend + Backend)
* Groq API (LLaMA model)
* python-dotenv

---

## 🔄 Frontend Workflow

1. User opens the Streamlit web application.
2. UI displays:

   * Topic input field
   * Tone selection dropdown
   * Content type selector
   * Word limit slider
3. User enters topic and selects preferences.
4. User clicks **Generate Content** button.
5. Generated content is displayed on the screen.

---

## ⚙️ Backend Workflow

1. Environment variables are loaded using `dotenv`.

2. Groq API client is initialized with API key.

3. User inputs are captured:

   * Topic
   * Tone
   * Content type
   * Word limit

4. A dynamic prompt is created using user inputs.

5. The prompt is sent to Groq API:

   * Model: `llama-3.1-8b-instant`
   * Input: structured instructions + topic

6. LLM processes the request.

7. AI generates content based on tone and format.

8. Output is returned to the application.

9. Content is displayed in Streamlit UI.

---

## 🔁 Data Flow (End-to-End)

User Input → Prompt Creation → Groq API → LLM Processing → Generated Content → UI Display

---

## 🧪 Example Use Cases

* Blog writing
* LinkedIn content creation
* Social media posts
* Marketing content generation
* Content ideation

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
Sensitive data is not uploaded to GitHub.

---

## 📚 What I Learned

* Building AI-based content generation apps
* Prompt engineering for controlling tone and format
* Using Streamlit for interactive UI
* Integrating Groq API for real-time responses
* Designing real-world AI applications

---

## 📌 Future Improvements

* Add content editing options
* Add SEO optimization suggestions
* Add export/download feature
* Improve UI design
* Add multi-language support

---

## 📷 Output

Generates structured and engaging content based on topic, tone, and selected format.

---

## 👩‍💻 Author

Meghana
