def main():
   get_twttr()

def get_twttr():
    tweets = input("Input: ")
    twttr = []
    vogais = ["A", "E", "I", "O", "U"]

    for caracter in tweets:
        if caracter.upper() not in vogais:
            twttr.append(caracter)
    
    print("Output", "".join(twttr))
main()