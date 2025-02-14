import streamlit as st
import os
import tempfile
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()  # loading the environment variable
import warnings

# Configure Google API Key
warnings.filterwarnings("ignore")
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Load model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", convert_system_message_to_human=True)

# Function to load PDF and get responses
def load_pdf_and_get_response(file):
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(file.getvalue())
        tmp_file_path = tmp_file.name

    pdf_loader = PyPDFLoader(tmp_file_path)
    pages = pdf_loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    context = "\n\n".join(str(p.page_content) for p in pages)
    texts = text_splitter.split_text(context)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_index = Chroma.from_texts(texts, embeddings).as_retriever(search_kwargs={"k":5})

    qa_chain = RetrievalQA.from_chain_type(
        model,
        retriever=vector_index,
        return_source_documents=True
    )

    question = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        result = qa_chain({"query": question})
        st.write(result["result"])

def main():
    st.title(" Q&A")
    file = st.file_uploader("Upload PDF file", type="pdf")
    if file is not None:
        load_pdf_and_get_response(file)

if __name__ == "__main__":
    main()   
