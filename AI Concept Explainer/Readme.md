

# 🎭 AI Concept Explainer

A prompt-based personality adaptation system built using **Python**, **Groq API**, and **Prompt Engineering**.

---

## 📖 Overview

AI Concept Explainer is an interactive system that explains complex topics in different audience styles using a single Large Language Model.

The project demonstrates how modifying **system prompts** dynamically changes the tone, vocabulary, and personality of AI responses — without changing the model itself.

---

## 🚀 Available Modes

* 🎩 Shakespeare
* 🏴‍☠️ Pirate
* 🤠 Bandit

The same topic is explained differently based on the selected style.

---

## ⚙️ How It Works

The system uses structured prompt engineering:

* **System Prompt** → Defines AI behaviour and personality rules
* **User Prompt** → Provides the topic to explain
* **Model** → Adapts output tone dynamically
* **Temperature Control** → Adds creativity to styled responses

---

## 🛠 Tech Stack

* Python
* Groq API
* LLaMA 3.1 Model
* openai Python SDK
* python-dotenv

---

## 📂 Project Structure

```
ai-concept-explainer/
│
├── app.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone <https://github.com/Ananya-Puthran/API-usage.git>
cd ai-concept-explainer
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

Make sure `.env` is included in `.gitignore` to protect your API key.

---

## ▶️ Run the Application

```bash
python app.py
```

You will see:

```
🎭 AI Concept Explainer
1. Shakespeare
2. Pirate
3. Bandit
```

Enter your choice and topic to receive a styled explanation.

---

## 🎯 Purpose of the Project

This project demonstrates:

* Prompt engineering techniques
* Personality-driven AI outputs
* API integration with Groq
* Secure environment variable handling
* CLI-based AI application design

---




