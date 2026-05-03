import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
import PyPDF2

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("📝 AI Text Summarizer")

st.write("Enter text or upload PDF to get summary")

# Summary type
summary_type = st.selectbox(
    "Select Summary Length",
    ["Short", "Medium", "Detailed"]
)

# Bullet points option
bullet = st.checkbox("Bullet Points Summary")

# Text input
text_input = st.text_area("Paste your text here")

# PDF upload
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

pdf_text = ""

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    for page in reader.pages:
        pdf_text += page.extract_text()

# Final text
final_text = text_input if text_input else pdf_text

if st.button("Generate Summary"):

    if final_text == "":
        st.warning("Please enter text or upload PDF")
    else:
        with st.spinner("Generating summary..."):

            prompt = f"""
            Summarize the following text.

            Length: {summary_type}

            {'Use bullet points.' if bullet else 'Write in paragraph form.'}

            Text:
            {final_text}
            """

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            summary = response.choices[0].message.content

            st.subheader("Summary:")
            st.write(summary)