def agent_reasoning(query, context):
    plan = f"""
You are an intelligent AI assistant.

Step 1: Understand the user query.
Step 2: Use the retrieved context.
Step 3: Provide structured and clear answer.

User Query:
{query}

Retrieved Context:
{context}

Now generate a structured response.
"""

    return plan