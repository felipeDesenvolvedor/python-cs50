def main():
   get_twttr(input("Input: "))

def get_twttr(tweets): 
    twttr = []
    vogais = ["A", "E", "I", "O", "U"]

    for caracter in tweets:
        if caracter.upper() not in vogais:
            twttr.append(caracter)
    
    print("Output", "".join(twttr))
    return "".join(twttr)

if __name__ == "__main__":
    main()