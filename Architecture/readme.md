

# 🏗 LLM Application Architecture

A modular Large Language Model pipeline built using Python, Groq API, and clean software engineering principles.

---

## 📖 Overview

LLM Application Architecture is a structured AI system that demonstrates how real-world GenAI applications are built using modular design.

Instead of writing everything in one script, this project separates responsibilities into layers — just like production-grade AI systems.

The system follows a structured pipeline:

User Input → Prompt Layer → LLM Layer → Post-Processing → Output

---

## 🚀 Architecture Flow

1️⃣ Input Layer
2️⃣ Prompt Layer
3️⃣ LLM Layer
4️⃣ Post-Processing Layer
5️⃣ Pipeline Orchestrator

Each component has a single responsibility.

---

## ⚙️ How It Works

The system follows a modular AI workflow:

Input Layer → Collects user input
Prompt Layer → Builds structured prompts
LLM Layer → Sends request to Groq via LiteLLM
Post-Processing → Cleans and formats response
Pipeline → Orchestrates the entire workflow

Each layer works independently, making the system scalable and maintainable.

---

## 🛠 Tech Stack

Python
Groq API
LLaMA 3.1 Model
LiteLLM
python-dotenv

---

## 📂 Project Structure

```
module3_architecture/
│
├── input_layer.py
├── prompt_layer.py
├── llm_layer.py
├── post_processing.py
├── pipeline.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Create Virtual Environment

Windows:
python -m venv venv
venv\Scripts\activate

### 2️⃣ Install Dependencies

pip install -r requirements.txt

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

GROQ_API_KEY=your_key_here


Make sure `.env` is added to `.gitignore`.

---

## ▶️ Run the Application

python pipeline.py

The system will execute the complete modular LLM workflow.

---

## 🎯 Purpose of the Project

This project demonstrates:

Modular AI architecture design
Separation of concerns
Prompt abstraction techniques
Model invocation layer design
Post-processing strategies
Production-style GenAI system thinking

