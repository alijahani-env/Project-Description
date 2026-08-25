


import streamlit as st
import PyPDF2
from groq import Groq

st.title("PDF Summary (Groq API)")

groq_api_key = st.text_input("Enter Groq API key:", type="password")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file and groq_api_key:

    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    if not text.strip():
        st.error("Could not extract text from this PDF.")
        st.stop()

    if st.button("Summarize PDF"):

        client = Groq(api_key=groq_api_key)

        try:
            completion = client.chat.completions.create(
                model="llama-3.1-70b-versatile",
                messages=[
                    {"role": "user", "content": f"Summarize this PDF:\n\n{text}"}
                ]
            )

            summary = completion.choices[0].message.content
            st.subheader("Summary")
            st.write(summary)

        except Exception as e:
            st.error("Groq API error occurred.")
            st.write(str(e))

elif uploaded_file and not groq_api_key:
    st.warning("Please enter a Groq API key.")


