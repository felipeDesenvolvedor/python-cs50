from random import randint

points = 0

def main():
    print(
        check_resolution(
            generate_operations(
                generate_integer(
                    get_level()
                )
            )
        )
    )


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if is_valid_level(level):
                return level
        except ValueError:
            continue

def check_resolution(operations):
    def sum_point():
        global points
        points += 1

    def message_error_response(retryNumber, operation):
        print("EEE")
        if retryNumber == 3:
            print(f"{operation['operation']} = {operation['result']}")

    def get_result_operation(operation):
        retryResponse = 1
    
        while retryResponse <= 3:
            try:
                responseCalc = input(f"{operation['operation']} = ")

                if int(responseCalc) == int(operation["result"]):
                    sum_point()
                    break
                message_error_response(retryResponse, operation)
            except ValueError:
                message_error_response(retryResponse, operation)

            retryResponse += 1

    for operation in operations:
        get_result_operation(operation)

    return points

def generate_operations(randomNumber):
    operations = []
    
    for _ in range(10):
        number1 = randint(1, randomNumber)
        number2 = randint(1, randomNumber)
        operations.append({"operation":f"{number1} + {number2}", "result":number1 + number2})

    return operations

def generate_integer(level):
    return randint(level, 10)

def is_valid_level(level):
    if level <= 0 or level >= 4:
        raise ValueError("Level must be 1, 2, or 3")
    return True


if __name__ == "__main__":
    main()