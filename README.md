

# 📄 AI PDF Reader Using OpenAI API


**AI PDF Reader** is a Streamlit web application that allows users to upload PDF documents and ask questions about their content using OpenAI's GPT model. The app uses LangChain, Hugging Face embeddings, and FAISS for document retrieval and context-aware Q&A.

---

## 🚀 Features

- Upload and read PDF files
- Extract and process text from PDFs
- Ask questions about the content of uploaded PDFs
- Uses `gpt-3.5-turbo` via OpenAI API for answering questions
- Fast similarity search using FAISS
- Embeddings powered by Hugging Face (`sentence-transformers/all-MiniLM-L6-v2`)

---



## 📦 Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Hugging Face Transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---



## ⚙️ Installation
1. **Clone the repository**
   
   git clone https://github.com/dishaAIML/ai-pdf-reader.git
   cd ai-pdf-reader


Create a virtual environment 


python -m venv .venv
source On Windows: .venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Add your OpenAI API key

Create a .env file in the root directory and add:


OPENAI_API_KEY=your_openai_api_key

▶️ Running the App

streamlit run app.py


📁 Project Structure

ai-pdf-reader/
│

├── app.py                 # Main Streamlit app

├── requirements.txt       # Python dependencies

├── .env                   # Environment variables

└── README.md              # Project documentation



🧠 How It Works
PDF is uploaded and text is extracted using PyPDF2.

Text is split into chunks for efficient processing.

Each chunk is embedded using Hugging Face sentence transformer.

FAISS indexes the vectors for similarity search.

When a user asks a question, relevant chunks are retrieved.

These chunks are passed to OpenAI's GPT model via LangChain for response.


![IMG-20250430-WA0001](https://github.com/user-attachments/assets/10062875-ee47-47e9-8f98-299b4f050601)
![IMG-20250430-WA0002](https://github.com/user-attachments/assets/a93b442b-4f82-4f76-879a-b40b2d000994)
![IMG-20250430-WA0003](https://github.com/user-attachments/assets/a36ba98a-ac85-4bce-a764-d5c1ea2744d3)
![IMG-20250430-WA0004](https://github.com/user-attachments/assets/dafbe165-c967-4f38-8f53-0ab389dec493)


