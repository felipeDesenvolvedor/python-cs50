def main():
    print(get_fractions())

def get_fractions():
    while True:
        try:
            fraction = input("Input a Fraction: ")
            numerador = get_parts_fractions(fraction)["numerador"]
            denominador = get_parts_fractions(fraction)["denominador"]

            if(chek_positive_numbers(numerador, denominador)):
                return get_status_tank((int(numerador) / int(denominador)) * 100)
        except Exception as e:
            return e 

def get_parts_fractions(param):
    return {"numerador":param.split("/")[0], "denominador":param.split("/")[1]}

def chek_positive_numbers(numerador, denominador):
    try:
        if int(denominador) == 0:
            raise ZeroDivisionError("You can't divide by zero!")
        
        if int(numerador) == 0:
            return True
        
        if int(numerador) <= int(denominador) and int(numerador) > 0:
            return True

    except Exception as e:
        raise e

def get_status_tank(quantity):
    if quantity <= 1:
        return f"<E>"
    elif quantity >= 99:
        return f"<F>"
    else:
        return f"Tank: {quantity}%"

main()