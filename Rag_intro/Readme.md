Introduction to RAG

A Retrieval-Augmented Generation (RAG) system built using Python, LiteLLM, and Groq API.

---

## 📖 Overview

**Retrieval-Augmented Generation (RAG)** — a hybrid AI architecture that combines document retrieval with Large Language Model generation.

Instead of relying solely on model memory, the system:

1. Retrieves relevant information from a local knowledge base
2. Passes the retrieved context to an LLM
3. Generates grounded answers based only on the provided context

This ensures more accurate, document-based responses and reduces hallucination.

---

## 🚀 What This Project Demonstrates

* Basic RAG pipeline architecture
* Keyword-based document retrieval
* Context-grounded LLM generation
* Prompt engineering for controlled outputs
* Secure API key handling using environment variables
* Modular AI system design

---

## ⚙️ How It Works

The pipeline follows three structured phases:

### 1️⃣ Retrieval Phase

* Loads documents from the `knowledge_base/` folder
* Performs simple keyword-based matching
* Extracts relevant context

### 2️⃣ Augmentation Phase

* Injects retrieved context into a structured prompt

### 3️⃣ Generation Phase

* Sends the prompt to Groq LLaMA 3.1 model via LiteLLM
* Generates an answer strictly based on retrieved context

The system prompt enforces this rule:

> “If the answer is not in context, say:
> 'I do not have enough information in the provided documents.'”

---

## 🛠 Tech Stack

* Python
* LiteLLM
* Groq API
* LLaMA 3.1 Model
* python-dotenv

---

## 📂 Project Structure

```
Rag_intro/
│
├── knowledge_base/
│   ├── ai_notes.txt
│   └── ml_notes.txt
│
├── retriever.py
├── llm_layer.py
├── rag_pipeline.py
├── main.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

### 📌 File Roles

* `knowledge_base/` → Text documents used for retrieval
* `retriever.py` → Loads documents and performs keyword-based search
* `llm_layer.py` → Handles interaction with LiteLLM + Groq
* `rag_pipeline.py` → Connects retrieval and generation
* `main.py` → CLI interface for asking questions

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/Ananya-Puthran/API-usage.git
cd API-usage/Rag_intro
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```
python -m venv .venv
.\.venv\Scripts\Activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Copy `.env.example` to `.env`:

```
cp .env.example .env
```

Then add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
MODEL_NAME=groq/llama-3.1-8b-instant
```

⚠️ Make sure `.env` is included in `.gitignore` to prevent exposing secrets.

---

## ▶️ Run the Application

```
python main.py
```

You will see:

```
Ask a question:
```

The system will display:

* Retrieved Context
* AI Answer

If the answer is not present in documents, it will respond:

> I do not have enough information in the provided documents.

---

## 🎯 Purpose of the Project

This module demonstrates:

* Core RAG architecture fundamentals
* Context-grounded AI generation
* Reducing hallucination in LLM outputs
* Modular AI project structuring
* Secure API-based AI integration

---

## 📌 Learning Outcome

By completing this module, you understand:

* How retrieval improves LLM reliability
* How to structure multi-layer AI systems
* How prompt engineering controls model behavior
* How to securely integrate external APIs

