from config import DOMAIN_OPTIONS

def process_input():
    print("\n🎯 Select a Domain:\n")

    for i, domain in enumerate(DOMAIN_OPTIONS, start=1):
        print(f"{i}. {domain.capitalize()}")

    try:
        choice = int(input("\nEnter the number corresponding to your choice: "))
        
        if choice < 1 or choice > len(DOMAIN_OPTIONS):
            raise ValueError
        
        domain = DOMAIN_OPTIONS[choice - 1]
    
    except ValueError:
        print("❌ Invalid selection. Please enter a valid number.")
        exit()

    query = input("\nEnter your query: ")

    return domain, query