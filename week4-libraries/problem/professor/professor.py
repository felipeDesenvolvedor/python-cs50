from random import randint


def main():
    print(get_level())


def get_level():

    while True:
        try:
            randomNumber = generate_integer(int(input("Level: ")))
            print("generate_number_operator", generate_number_operator(randomNumber))
            return randomNumber
        except ValueError:
            continue

def generate_number_operator(level):
    operations = []

    for i in range(10):
        number1 = randint(1, level)
        number2 = randint(1, level)
        operations.append({"operation":f"{number1} + {number2}", "result":number1 + number2})
    return operations

def generate_integer(level):
    if level == 1 or level == 2 or level == 3:
        return randint(level, 10)
    else:
        raise ValueError("Level must be 1, 2, or 3")


if __name__ == "__main__":
    main()