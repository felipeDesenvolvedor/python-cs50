from random import randint

def main():
    get_number()

def get_number():
    randomNumber = randint(1, get_level())
    get_guess(randomNumber)

def get_guess(randomNumber):
    while True:
            try:
                numberGuess = int(input("Guess: "))
    
                if not numberGuess > 0:
                    continue
    
                if numberGuess < randomNumber:
                    print("Too small!")
                    continue
    
                if numberGuess > randomNumber:
                    print("Too large!")
                    continue
    
                if numberGuess == randomNumber:
                    print("Just right!")
                    break    
            except ValueError:
                continue

def get_level():
    numberLevel = 0
    while True:
        try:
            numberLevel = int(input("Level: "))

            if not numberLevel > 0:
                continue
            return numberLevel
        except ValueError:
            continue


if __name__ == "__main__":
    main()