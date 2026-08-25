
import streamlit as st
import PyPDF2
import requests
pip install PyPDF2


st.title("Copilot PDF Summarizer")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    # Extract PDF text
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    st.write("PDF uploaded successfully.")

    if st.button("Summarize with Copilot"):
        # Replace with your Copilot API endpoint + auth
        api_url = "https://api.copilot.microsoft.com/openai/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_API_KEY"
        }

        payload = {
            "model": "gpt-4o",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Summarize the following document:\n\n{text}"
                }
            ]
        }

        response = requests.post(api_url, headers=headers, json=payload)
        result = response.json()

        summary = result["choices"][0]["message"]["content"]
        st.subheader("Summary")
        st.write(summary)
