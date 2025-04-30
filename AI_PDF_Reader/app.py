from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI  # ✅ Updated import


# Load environment variables
load_dotenv()

# Prevent library error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

def extract_text_from_pdf(pdf):
    """Extract text from uploaded PDF file."""
    pdf_reader = PdfReader(pdf)
    return "\n".join(page.extract_text() or "" for page in pdf_reader.pages)

def process_text(text):
    """Split text and create vector embeddings using Hugging Face."""
    if not text.strip():
        return None

    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    chunks = text_splitter.split_text(text)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_texts(chunks, embeddings)

def answer_question(knowledge_base, user_question):
    """Find relevant answers from the knowledge base."""
    if not knowledge_base:
        return "Error: No valid content extracted from the PDF."

    docs = knowledge_base.similarity_search(user_question)

    # ✅ Updated to use ChatOpenAI instead of deprecated OpenAI
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

    chain = load_qa_chain(llm, chain_type="stuff")
    response = chain.run(input_documents=docs, question=user_question)
    return response

def main():
    st.set_page_config(page_title="Ask your PDF", page_icon="📄")
    st.header("Ask your PDF 💬")

    pdf = st.file_uploader("Upload your PDF", type="pdf")

    if pdf:
        text = extract_text_from_pdf(pdf)
        knowledge_base = process_text(text)

        if knowledge_base:
            user_question = st.text_input("Ask a question about your PDF:")
            if user_question:
                response = answer_question(knowledge_base, user_question)
                st.write(response)
        else:
            st.error("No text could be extracted from the PDF. Try a different file.")

if __name__ == '__main__':
    main()
