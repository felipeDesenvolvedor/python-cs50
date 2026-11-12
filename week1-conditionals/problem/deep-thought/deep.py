def main():
    print(valid_input(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")))

def valid_input(inputMessage):
    
    if inputMessage.strip() == "42" or inputMessage.lower().strip() == "forty-two" or inputMessage.lower().strip() == "forty two":
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    main()