import sys
import re

def main():
    print(get_fractions())

def get_fractions():

    fraction = input("Input a Fraction: ")
    
    if re.search(r"^([0-9]+)-([0-9]+)$", fraction):
        sys.exit()

    while True:
        try:

            if not fraction:
                fraction = input("Input a Fraction: ")
            
            if re.search(r"^([0-9]+)-([0-9]+)$", fraction):
                sys.exit()

            numerador = get_parts_fractions(fraction)["numerador"]
            denominador = get_parts_fractions(fraction)["denominador"]

            return gauge(convert(numerador, denominador))
        except (ValueError, ZeroDivisionError) as e:
            fraction = ""
            print(e) 

def get_parts_fractions(param):
    return {"numerador":param.split("/")[0], "denominador":param.split("/")[1]}

def convert(numerador, denominador):

    if int(denominador) == 0:
        raise ZeroDivisionError("You can't divide by zero!")

    if int(numerador) < 0:
        raise ValueError("Numerator must be greater than zero")    

    if int(numerador) <= int(denominador):
        return (int(numerador) / int(denominador)) * 100
    else:
        raise ValueError("Numerator must be smaller than zero")

def gauge(quantity):
    if quantity <= 1:
        return f"E"
    elif quantity >= 99:
        return f"F"
    else:
        return f"{quantity:.0f}%"

if __name__ == "__main__":
    main()