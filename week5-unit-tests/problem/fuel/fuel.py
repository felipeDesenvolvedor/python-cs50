def main():
    get_fractions()

def get_fractions():
    while True:
        try:
            fraction = input("Input a Fraction: ")
            numerador = get_parts_fractions(fraction)["numerador"]
            denominador = get_parts_fractions(fraction)["denominador"]

            if(chek_positive_numbers(numerador, denominador)):
                get_porcentage(numerador, denominador)
                break
        except Exception as e:
            print("An error occurred:", e) 

def get_porcentage(numerador, denominador):
    try:
        get_status_tank((int(numerador) / int(denominador)) * 100)
    except ZeroDivisionError:
        print("You can't divide by zero!")   

def get_parts_fractions(param):
    return {"numerador":param.split("/")[0], "denominador":param.split("/")[1]}

def chek_positive_numbers(numerador, denominador):
    try:
        if int(numerador) == 0:
            return True
        
        if int(numerador) <= int(denominador) and int(numerador) > 0:
            return True
    except:
        print("Not a number integer")
        return False

def get_status_tank(quantity):
    if quantity <= 1:
        print(f"<E>")
    elif quantity >= 99:
        print(f"<F>")
    else:
        print(f"Tank: {quantity}%") 

main()