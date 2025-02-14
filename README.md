# PDF Q&A Explorer: Dual Approach Edition 🚀

Welcome to the **PDF Q&A Explorer** repository! This project offers **two unique implementations** to help you extract and explore insights from your PDF documents using advanced AI:

- **LangChain Approach:** Powered by LangChain and Google Generative AI.
- **LlamaIndex Approach:** Leverages the efficiency of LlamaIndex for indexing and retrieval.

Choose your preferred method or explore both to see which best fits your needs!

---

## 📚 What Does It Do?

This application transforms static PDF documents into interactive knowledge bases. Upload a PDF, ask questions about its content, and receive detailed, AI-generated answers—whether you prefer the LangChain or LlamaIndex pipeline.

---

## 🗂️ Repository Overview

- **langchain_app.py:**  
  Implements the Q&A functionality using LangChain. It extracts text from PDFs, splits it into chunks, embeds the text using Google Generative AI, and retrieves context-aware answers.

- **llamaindex_app.py:**  
  Implements the Q&A functionality using LlamaIndex. It focuses on efficient indexing of PDF content to quickly respond to your queries.

---

## 🚀 Features

- **Intuitive Interface:** Streamlit-powered UI for easy document uploads and question submission.
- **AI-Driven Responses:** Get insightful answers using cutting-edge AI models.
- **Dual Implementations:** Explore two different approaches—LangChain for a retrieval-based pipeline and LlamaIndex for efficient document indexing.
- **Open Source:** Customize and extend the applications to fit your specific needs.

---

## 🛠️ Getting Started

### Prerequisites

Make sure you have Python installed and then install the necessary dependencies:

```bash
pip install streamlit langchain chromadb langchain_google_genai google-generativeai python-dotenv PyPDF2 llama-index
