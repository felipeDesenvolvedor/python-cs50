from random import randint

points = 0

def main():
    print(
        check_resolution(
            generate_operations(
                get_level()
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
                responseCalc = input(f"{operation['operation']}")

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

def generate_operations(level):
    randomNumber = generate_integer(level)
    operations = []

    def generate_operation(start, end):
        number1 = randint(start, end)
        number2 = randint(start, end)
        operations.append({"operation":f"{number1} + {number2} =", "result":number1 + number2})
        return operations
    
    for _ in range(10):
        if level == 1:
            return generate_operation(0, randomNumber)
        if level == 2:
            return generate_operation(10, randomNumber)
        if level == 3:
            return generate_operation(100, randomNumber)

    return operations

def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    if level == 2:
        return randint(10, 99)
    if level == 3:
        return randint(100, 990)

def is_valid_level(level):
    if level <= 0 or level >= 4:
        raise ValueError("Level must be 1, 2, or 3")
    return True


if __name__ == "__main__":
    main()