

import streamlit as st
import PyPDF2
from groq import Groq

st.title("PDF Summarizer (Groq API – Free)")

# User enters their Groq API key
groq_api_key = st.text_input("Enter your Groq API key:", type="password")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file and groq_api_key:

    # Extract PDF text
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    if st.button("Summarize PDF"):

        client = Groq(api_key=groq_api_key)

        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": f"Summarize this PDF:\n\n{text}"}
            ]
        )

        summary = completion.choices[0].message.content

        st.subheader("Summary")
        st.write(summary)

elif uploaded_file and not groq_api_key:
    st.warning("Please enter your Groq API key to continue.")

