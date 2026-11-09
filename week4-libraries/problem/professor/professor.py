from random import randint


def main():
    print(get_level())


def get_level():

    while True:
        try:
            randomNumber = generate_integer(int(input("Level: ")))
            return check_resolution(generate_number_operator(randomNumber))
        except ValueError:
            continue

def check_resolution(operations):
    points = 0

    for i in operations:
        retryResponse = 1

        def message_error_response(retryNumber):
            print("EEE")
            if retryNumber == 3:
                print(f"{i['operation']} = {i['result']}")

        while retryResponse <= 3:
            try:
                responseCalc = input(f"{i['operation']} = ")

                if int(responseCalc) == int(i["result"]):
                    points += 1
                    break
                else:
                    message_error_response(retryResponse)
            except ValueError:
                message_error_response(retryResponse)

            retryResponse += 1


    print(f"{points}")

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