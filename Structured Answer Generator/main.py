import os
import json
from dotenv import load_dotenv
from litellm import completion
from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Take user input
user_question = input("Enter your question: ")
temperature = float(input("Enter temperature (0 to 1): "))

# Call LiteLLM with Groq
response = completion(
    model="groq/llama-3.1-8b-instant",  # You can change model
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_question}
    ],
    temperature=temperature,
    api_key=groq_api_key
)

# Extract output
output_text = response["choices"][0]["message"]["content"]

# Validate JSON
try:
    structured_output = json.loads(output_text)
    print("\n✅ Structured Output:\n")
    print(json.dumps(structured_output, indent=4))
except json.JSONDecodeError:
    print("\n⚠ Model did not return valid JSON:")
    print(output_text)