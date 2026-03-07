
# Domain Specific GenAI

A multi-domain AI system built using Python, Groq API, RAG (Retrieval-Augmented Generation), Agent Reasoning, and Evaluation Layers.

---

## 📖 Overview

Domain Specific GenAI is an advanced AI architecture that combines:

* Retrieval-Augmented Generation (RAG)
* Agent-based reasoning
* Large Language Model generation
* Output evaluation scoring

The system dynamically processes user queries across multiple domains using a structured AI pipeline.

This project demonstrates how modern AI systems are architected in real-world applications — beyond simple prompt calls.

---

## 🚀 Available Domains

🎓 Academic Assistant
💼 Placement AI Assistant
📄 Research Paper Explainer
💻 Coding Debug Assistant
🚀 Startup Idea Evaluation

Each domain uses domain-specific knowledge files for retrieval.

---

## 🔁 System Architecture

User Input
↓
Input Layer
↓
Retriever (RAG)
↓
Agent Reasoning
↓
LLM Generation
↓
Evaluation Layer
↓
Final Structured Output

---

## ⚙️ How It Works

The system follows a structured AI pipeline:

### 1️⃣ Input Layer

* Accepts user query
* Validates selected domain

### 2️⃣ Retriever (RAG)

* Loads domain-specific knowledge
* Performs keyword-based retrieval
* Injects relevant context into the prompt

### 3️⃣ Agent Reasoning Layer

* Breaks the task into logical steps
* Creates structured instructions for the LLM

### 4️⃣ LLM Layer

* Uses Groq LLaMA 3.1 model
* Generates structured response
* Controlled temperature for accuracy

### 5️⃣ Evaluation Layer

* Scores output based on:

  * Length
  * Structure
  * Completeness

---

## 🛠 Tech Stack

* Python
* Groq API
* LLaMA 3.1 Model
* LiteLLM
* python-dotenv
* Prompt Engineering
* RAG (Keyword-based Retrieval)

---

## 📂 Project Structure

```
Domain-Specific-GenAI/
│
├── main.py
├── config.py
├── input_layer.py
├── retriever.py
├── agent.py
├── llm_layer.py
├── evaluator.py
│
├── knowledge_base/
│     ├── academic.txt
│     ├── placement.txt
│     ├── research.txt
│     ├── coding.txt
│     └── startup.txt
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/Ananya-Puthran/API-usage.git
cd Domain-Specific-GenAI
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

⚠️ Make sure `.env` is added to `.gitignore` to protect your API key.

---

## ▶️ Run the Application

```
python main.py
```

You will see:

```
Available Domains: ['academic', 'placement', 'research', 'coding', 'startup']
Choose domain:
Enter your query:
```

The system will generate a structured AI response along with an evaluation score.

---

## 🎯 Purpose of the Project

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Agent-based structured reasoning
* Multi-domain AI architecture
* Evaluation and response scoring
* Secure API key handling
* Modular AI system design
* Production-style pipeline orchestration

---

## 🧠 What Makes This Project Advanced?

Unlike simple chatbot projects, this system includes:

✔ Context retrieval
✔ Reasoning layer
✔ Model abstraction
✔ Output evaluation
✔ Domain modularity

This is close to real-world AI system architecture used in production systems.

