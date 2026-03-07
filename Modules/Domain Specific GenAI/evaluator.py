def evaluate_response(response):
    score = 0

    if len(response) > 100:
        score += 1
    if "Step" in response or "•" in response:
        score += 1
    if len(response.split()) > 50:
        score += 1

    return score