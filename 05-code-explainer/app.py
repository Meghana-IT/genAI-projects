import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load API
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("💻 AI Code Explainer")

st.write("Paste your code and get a simple explanation")

# Code input
code_input = st.text_area("Enter your code here")

# Mode selection
mode = st.selectbox(
    "Select Explanation Mode",
    ["Beginner", "Advanced"]
)

# Bug detection option
bug_check = st.checkbox("Check for bugs and improvements")

if st.button("Explain Code"):

    if code_input == "":
        st.warning("Please enter code")
    else:
        with st.spinner("Analyzing code..."):

            prompt = f"""
            Explain the following code in {mode} level.

            Code:
            {code_input}

            Also:
            {'Check for bugs and suggest improvements.' if bug_check else ''}

            Give step-by-step explanation.
            """

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            explanation = response.choices[0].message.content

            st.subheader("Explanation:")
            st.write(explanation)