

# 📌 Structured Answer Generator

A production-style structured response generator built using **LiteLLM**, **Groq API**, and **Prompt Engineering**.

---

## 📖 Overview

This project generates structured and deterministic JSON responses from a Large Language Model (LLM).

It ensures:

* Controlled output format
* Stable and predictable responses
* Separation of system and user prompts
* Production-ready architecture

---

## 🚀 Features

* ✅ Controlled JSON output format
* ✅ Deterministic prompting (temperature control)
* ✅ Production-style prompt separation
* ✅ Environment variable configuration
* ✅ Modular and clean code structure

---

## 🛠 Tech Stack

* Python
* LiteLLM
* Groq API
* python-dotenv

---

## 📂 Project Structure

```
structured-answer-generator/
│
├── main.py
├── prompts.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd structured-answer-generator
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here

```

Make sure your API key is valid and active.

---

## ▶️ Run the Application

```bash
python main.py
```

You will be prompted to enter:

* Your question
* Temperature value (0–1)

The system will return a structured JSON response.

---

## 📄 Output Format

The model strictly returns:

```json
{
  "title": "",
  "definition": "",
  "key_points": [],
  "example": "",
  "summary": ""
}
```

---

## 🎯 Purpose of the Project

This project demonstrates:

* LLM orchestration
* API integration
* Prompt engineering
* Deterministic AI output control
* Production-ready AI system design

---
