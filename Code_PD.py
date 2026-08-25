


import streamlit as st
import PyPDF2
import requests

st.title("PDF Summarizer")

# Let user enter their own API key
user_api_key = st.text_input("Enter your OpenAI API key:", type="password")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file and user_api_key:

    # Extract PDF text
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # Summarize button
    if st.button("Summarize PDF"):

        api_url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {user_api_key}"
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "user", "content": f"Summarize this document:\n\n{text}"}
            ]
        }

        response = requests.post(api_url, headers=headers, json=payload)
        result = response.json()

        if "choices" in result:
            summary = result["choices"][0]["message"]["content"]
            st.subheader("Summary")
            st.write(summary)
        else:
            st.error("API Error:")
            st.write(result)

elif uploaded_file and not user_api_key:
    st.warning("Please enter your OpenAI API key to continue.")
