from input_layer import process_input
from retriever import retrieve_context
from agent import agent_reasoning
from llm_layer import call_llm
from evaluator import evaluate_response


def main():
    domain, query = process_input()

    print("\nRetrieving context...")
    context = retrieve_context(domain, query)

    print("Agent reasoning...")
    plan = agent_reasoning(query, context)

    print("Calling LLM...")
    response = call_llm(plan)

    print("\nEvaluating response...")
    score = evaluate_response(response)

    print("\n==================== FINAL OUTPUT ====================")
    print(response)
    print("\nEvaluation Score:", score, "/ 3")


if __name__ == "__main__":
    main()