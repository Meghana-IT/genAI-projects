# 📝 AI Text Summarizer

## 📌 Objective

The objective of this project is to build an AI-powered application that can summarize long text or PDF documents into short, meaningful content.
It helps users quickly understand large amounts of information without reading the full text.

---

## 🚀 Features

* Summarizes long text into concise output
* Supports PDF file upload
* Multiple summary lengths:

  * Short
  * Medium
  * Detailed
* Optional bullet-point summary
* AI-generated intelligent summaries
* Simple and interactive web interface

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

   * Text input box
   * PDF upload option
   * Summary length selector
   * Bullet point checkbox
3. User either:

   * Pastes text OR
   * Uploads a PDF file
4. User selects summary type (Short / Medium / Detailed).
5. User clicks **Generate Summary** button.
6. Output summary is displayed on the screen.

---

## ⚙️ Backend Workflow

1. Environment variables are loaded using `dotenv`.

2. Groq API client is initialized using the API key.

3. If a PDF is uploaded:

   * PyPDF2 reads the file
   * Extracts text from all pages

4. System checks:

   * If text input is available → use it
   * Else → use extracted PDF text

5. A dynamic prompt is created based on:

   * Summary length
   * Bullet point option

6. The prompt is sent to Groq API:

   * Model: `llama-3.1-8b-instant`
   * Input: user text + instructions

7. AI model processes the content.

8. A summarized response is generated.

9. The summary is displayed in the UI.

---

## 🔁 Data Flow (End-to-End)

User Input / PDF → Text Extraction → Prompt Creation → Groq API → LLM Processing → Summary → UI Display

---

## 🧪 Example Use Cases

* Summarizing articles
* Quick understanding of research papers
* Reading large PDFs in less time
* Students preparing notes
* Professionals analyzing reports

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
Sensitive information is not uploaded to GitHub.

---

## 📚 What I Learned

* Handling user input and file uploads in Streamlit
* Extracting text from PDFs using PyPDF2
* Creating dynamic prompts for AI summarization
* Integrating Groq API for real-time AI responses
* Designing user-friendly interfaces
* Managing data flow in AI applications

---

## 📌 Future Improvements

* Add support for DOCX files
* Highlight key points in summary
* Add download option for summary
* Improve UI design
* Add multi-language support

---

## 📷 Output

Displays summarized text based on user input or uploaded PDF with adjustable length and format.

---

## 👩‍💻 Author

Meghana
