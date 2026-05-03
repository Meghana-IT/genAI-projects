# 💻 AI Code Explainer

## 📌 Objective

The objective of this project is to build an AI-powered application that explains programming code in simple and understandable language.
It helps beginners and developers understand code logic, flow, and structure with step-by-step explanations.

---

## 🚀 Features

* Code input box for multiple programming languages
* Step-by-step code explanation
* Two explanation modes:

  * 👶 Beginner (simple explanations)
  * 🧠 Advanced (technical explanations)
* Optional bug detection and improvement suggestions
* AI-generated explanations
* Interactive and user-friendly interface

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

   * Code input text area
   * Mode selection dropdown (Beginner / Advanced)
   * Bug detection checkbox
   * Explain button
3. User pastes code.
4. User selects explanation mode.
5. User optionally enables bug detection.
6. User clicks **Explain Code**.
7. Explanation is displayed on the screen.

---

## ⚙️ Backend Workflow

1. Environment variables are loaded using `dotenv`.

2. Groq API client is initialized with API key.

3. User inputs are captured:

   * Code
   * Explanation mode
   * Bug detection preference

4. A dynamic prompt is created:

   * Based on selected mode
   * Includes instructions for explanation
   * Includes optional bug analysis

5. Request is sent to Groq API:

   * Model: `llama-3.1-8b-instant`
   * Input: user code + instructions

6. LLM processes the code.

7. AI generates:

   * Step-by-step explanation
   * Bug suggestions (if enabled)

8. Output is returned.

9. Explanation is displayed in Streamlit UI.

---

## 🔁 Data Flow (End-to-End)

User Code → Prompt Creation → Groq API → LLM Processing → Explanation → UI Display

---

## 🧪 Example Use Cases

* Learning programming concepts
* Understanding unfamiliar code
* Debugging and improving code
* Teaching beginners
* Interview preparation

---

## ▶️ How to Run

### Step 1: Install dependencies

```bash id="s4t9d0"
pip install -r requirements.txt
```

### Step 2: Add API Key

Create a `.env` file and add:

```env id="shy3re"
GROQ_API_KEY=your_api_key_here
```

### Step 3: Run the app

```bash id="1tfkqp"
streamlit run app.py
```

---

## 🔐 Security Note

The `.env` file is excluded using `.gitignore` to protect the API key.
Sensitive data is not uploaded to GitHub.

---

## 📚 What I Learned

* Building AI-powered developer tools
* Prompt engineering for code explanation
* Handling structured input (code) with LLMs
* Designing beginner-friendly AI systems
* Integrating API-based AI models into applications

---

## 📌 Future Improvements

* Add syntax highlighting
* Support file upload (.py, .java, etc.)
* Add code execution feature
* Improve UI design
* Add multi-language explanations

---

## 📷 Output

Displays clear, structured, and step-by-step explanations of input code with optional bug analysis.

---

## 👩‍💻 Author

Meghana
