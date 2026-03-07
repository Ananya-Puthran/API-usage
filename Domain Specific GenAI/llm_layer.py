import os
from dotenv import load_dotenv
import litellm

load_dotenv()

litellm.api_key = os.getenv("GROQ_API_KEY")

def call_llm(prompt):
    response = litellm.completion(
        model="groq/llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response["choices"][0]["message"]["content"]