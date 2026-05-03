import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
import PyPDF2

# Load API
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and compare with job description")

# Upload resume
resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

# Job description input
job_desc = st.text_area("Paste Job Description")

resume_text = ""

# Extract resume text
if resume_file:
    reader = PyPDF2.PdfReader(resume_file)
    for page in reader.pages:
        resume_text += page.extract_text()

if st.button("Analyze Resume"):

    if resume_text == "" or job_desc == "":
        st.warning("Please upload resume and enter job description")
    else:
        with st.spinner("Analyzing..."):

            prompt = f"""
            Compare the following resume with the job description.

            Resume:
            {resume_text}

            Job Description:
            {job_desc}

            Give output in this format:

            1. Match Score (percentage)
            2. Missing Skills
            3. Improvement Suggestions
            4. Suggested Resume Bullet Points
            """

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            result = response.choices[0].message.content

            st.subheader("Analysis Result")
            st.write(result)