from config import DOMAIN_OPTIONS

def process_input():
    print("Available Domains:", DOMAIN_OPTIONS)
    domain = input("Choose domain: ").lower()

    if domain not in DOMAIN_OPTIONS:
        raise ValueError("Invalid domain selected.")

    query = input("Enter your query: ")

    return domain, query