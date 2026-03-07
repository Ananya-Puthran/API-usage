import os

def load_knowledge(domain):
    path = f"knowledge_base/{domain}.txt"

    if not os.path.exists(path):
        return ""

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def retrieve_context(domain, query):
    knowledge = load_knowledge(domain)

    # Simple keyword matching
    relevant_chunks = []
    for line in knowledge.split("\n"):
        if any(word.lower() in line.lower() for word in query.split()):
            relevant_chunks.append(line)

    return "\n".join(relevant_chunks[:5])  # return top 5 lines