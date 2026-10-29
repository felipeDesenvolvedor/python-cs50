def main():
    print(bank_tip(input("Greeting")))

def bank_tip(message):

    if message.lower().startswith("hello"):
        return "$0"
    
    if message.lower().startswith("h"):
        return "$20"
    
    return "$100"

if __name__ == "__main__":
    main()