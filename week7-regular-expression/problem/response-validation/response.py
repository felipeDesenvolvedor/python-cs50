from validator_collection import checkers

def main():
    print(validat_email("malan@@@harvard.edu"))

def validat_email(email):
    return "Valid" if checkers.is_email(email) else "Invalid"
    
if __name__ == "__main__":
    main()