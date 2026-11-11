def main():
   print(shorten(input("Input: ")))

def shorten(tweets): 
    twttr = []
    vogais = ["A", "E", "I", "O", "U"]

    for caracter in tweets:
        if caracter.upper() not in vogais:
            twttr.append(caracter)

    return "".join(twttr)

if __name__ == "__main__":
    main()