from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

def get_explanation(topic, style):

    system_prompt = f"""
You are an AI Concept Explainer.

When style is Shakespeare:
Use old English vocabulary and dramatic tone.

When style is Pirate:
Use sea slang and pirate accent.

When style is Bandit:
Use rugged outlaw language.

Current style: {style}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Explain the concept of {topic}."}
        ],
        temperature=0.9
    )

    return response.choices[0].message.content


def main():
    print("\n🎭 AI Concept Explainer")
    print("1. Shakespeare")
    print("2. Pirate")
    print("3. Bandit")

    choice = input("\nEnter your choice (1/2/3): ")
    topic = input("Enter the topic: ")

    styles = {
        "1": "Shakespeare",
        "2": "Pirate",
        "3": "Bandit"
    }

    style = styles.get(choice)

    if not style:
        print("Invalid choice!")
        return

    explanation = get_explanation(topic, style)

    print("\n📚 Explanation:\n")
    print(explanation)


if __name__ == "__main__":
    main()