# Resume Review AI Agent

A structured AI Agent built using Python, LiteLLM, and Groq API to simulate multi-step reasoning for resume evaluation.

---

## 📖 Overview

**Resume Review AI Agent** is a mini-project that demonstrates core AI Agent concepts through a practical application.

Instead of directly asking an LLM to review a resume, this system breaks the task into structured reasoning steps:

* Extract skills
* Compare resume with job description
* Suggest improvements
* Score the resume

This mirrors how real-world AI agents perform **task decomposition and tool usage** before generating intelligent outputs.

---

## 🤖 Agent Workflow

```
User Input (Resume + Job Description)
        ↓
Step 1: Extract Skills (Tool Simulation)
        ↓
Step 2: Compare Skills (Tool Simulation)
        ↓
Step 3: Suggest Improvements (LLM Reasoning)
        ↓
Step 4: Score Resume (LLM Evaluation)
```

The agent does not rely on a single prompt — it orchestrates tools and reasoning in a structured pipeline.

---

## 🧠 What You’ll Learn

This module teaches foundational AI Agent thinking:

* What is an AI Agent
* Multi-step reasoning
* Task decomposition
* Tool simulation
* Structured workflow design
* LLM orchestration using LiteLLM

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
resume-review-ai-agent/
│
├── main.py              # CLI interface
├── agent_brain.py       # Core agent orchestration logic
├── tools.py             # Simulated tools (skill extraction & comparison)
├── llm_layer.py         # LiteLLM interaction layer
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

### 🔹 Step 1 – Skill Extraction

A simulated tool extracts keywords and technical skills from the resume and job description.

### 🔹 Step 2 – Skill Comparison

The system compares overlapping and missing skills.

### 🔹 Step 3 – Suggest Improvements

The LLM provides structured feedback on:

* Missing skills
* Resume clarity
* Improvement suggestions

### 🔹 Step 4 – Resume Scoring

The LLM assigns a score based on alignment with the job description.

This demonstrates **Agent + Tool + LLM hybrid reasoning architecture**.

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ananya-Puthran/API-usage.git
cd "Resume review AI"
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

Make sure `.env` is added to `.gitignore` to protect your API key.

---

## ▶️ Run the Application

```bash
python main.py
```

You will be prompted to enter:

* Resume text
* Job description

The agent will then perform structured analysis and provide feedback with scoring.

---

## 🎯 Purpose of This Project

This project demonstrates:

* AI Agent workflow design
* Structured reasoning instead of single-prompt LLM calls
* Real-world automation thinking
* Tool + LLM orchestration
* Clean modular project architecture

---

## 🚀 Why This Project Matters

This is not just a resume reviewer.
It is a foundational example of **how AI agents think, break problems into steps, and use tools intelligently** — which is the core idea behind modern AI automation systems.
