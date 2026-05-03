# 📄 AI Resume Analyzer

## 📌 Objective

The objective of this project is to build an AI-powered application that analyzes a resume against a given job description.
It helps job seekers identify skill gaps and improve their resumes for better alignment with job requirements and ATS systems.

---

## 🚀 Features

* Upload resume in PDF format
* Input job description
* AI-based resume analysis
* Match score (percentage)
* Missing skills identification
* Improvement suggestions
* Suggested resume bullet points
* Simple and interactive UI

---

## 🛠️ Technologies Used

* Python
* Streamlit (Frontend + Backend)
* Groq API (LLaMA model)
* PyPDF2 (for PDF text extraction)
* python-dotenv

---

## 🔄 Frontend Workflow

1. User opens the Streamlit web application.
2. UI displays:

   * Resume upload option (PDF)
   * Job description input box
   * Analyze button
3. User uploads resume.
4. User pastes job description.
5. User clicks **Analyze Resume**.
6. Analysis results are displayed on the screen.

---

## ⚙️ Backend Workflow

1. Environment variables are loaded using `dotenv`.

2. Groq API client is initialized with API key.

3. Uploaded PDF is processed using PyPDF2:

   * Reads file
   * Extracts text from each page

4. Resume text and job description are combined.

5. A structured prompt is created with instructions:

   * Match score
   * Missing skills
   * Suggestions
   * Resume improvements

6. Request is sent to Groq API:

   * Model: `llama-3.1-8b-instant`
   * Input: resume + job description

7. LLM processes and compares both inputs.

8. AI generates:

   * Match percentage
   * Missing skills
   * Suggestions

9. Output is displayed in Streamlit UI.

---

## 🔁 Data Flow (End-to-End)

Resume PDF → Text Extraction → Job Description Input → Prompt Creation → Groq API → LLM Processing → Analysis → UI Display

---

## 🧪 Example Use Cases

* Resume optimization for job applications
* ATS (Applicant Tracking System) improvement
* Skill gap analysis
* Interview preparation
* Career guidance

---

## ▶️ How to Run

### Step 1: Install dependencies

```bash id="vkmkql"
pip install -r requirements.txt
```

### Step 2: Add API Key

Create a `.env` file and add:

```env id="o8r8ha"
GROQ_API_KEY=your_api_key_here
```

### Step 3: Run the app

```bash id="u6g6nf"
streamlit run app.py
```

---

## 🔐 Security Note

The `.env` file is excluded using `.gitignore` to protect the API key.
Sensitive data is never uploaded to GitHub.

---

## 📚 What I Learned

* Extracting text from PDFs using PyPDF2
* Building AI-powered applications with Streamlit
* Prompt engineering for resume analysis
* Comparing structured and unstructured data using LLMs
* Designing real-world AI use cases
* Secure handling of API keys

---

## 📌 Future Improvements

* Add support for DOCX resumes
* Improve scoring accuracy
* Add keyword highlighting
* Add resume upload preview
* Deploy application online

---

## 📷 Output

Displays resume analysis including match score, missing skills, and improvement suggestions based on job description.

---

## 👩‍💻 Author

Meghana
