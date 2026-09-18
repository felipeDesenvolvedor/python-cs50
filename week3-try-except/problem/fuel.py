# Os indicadores de combustível mostram, geralmente com frações, a quantidade exata de combustível no tanque. Por exemplo, 1/4 indica que o tanque está 25% cheio, 1/2 indica que o tanque está 50% cheio e 3/4 indica que o tanque está 75% cheio.
# Em um arquivo chamado fuel.py, implemente um programa que solicite ao usuário uma fração, formatada como X/Y, onde Xé um inteiro não negativo e Yé um inteiro positivo, e então imprima, como uma porcentagem arredondada para o inteiro mais próximo, a quantidade de combustível restante no tanque. Se, no entanto, restar 1% ou menos, imprima E para indicar que o tanque está praticamente vazio. E se restar 99% ou mais, imprima F para indicar que o tanque está praticamente cheio.
# Se, no entanto, X`n` Y não for um número inteiro, X for maior que `n` Y, ou Y for `n` 0, solicite novamente ao usuário. (Não é necessário que ` Y n` seja `n` 4.) Certifique-se de capturar quaisquer exceções como `NULL` ValueErrorou `NULL`

# Requisitos
# OK) Em um arquivo chamado fuel.py, implemente um programa que solicite ao usuário uma fração, formatada como X/Y
# OK) X é um inteiro não negativo e Y é um inteiro positivo
# OK) então imprima, como uma porcentagem arredondada para o inteiro mais próximo, a quantidade de combustível restante no tanque.
# OK) Se, no entanto, restar 1% ou menos, imprima E
# OK) se restar 99% ou mais, imprima F para indicar que o tanque está praticamente cheio.
# 6) Se, no entanto, X `n` Y não for um número inteiro, solicite novamente ao usuário.
# OK) se X for maior que `n` Y, ou Y for `n` 0, solicite novamente ao usuário. solicite novamente ao usuário.
# 8) Certifique-se de capturar quaisquer exceções como `NULL` ValueErrorou `NULL` Zero DivisionError.

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
        return int(numerador) <= int(denominador) and int(numerador) > 0
    except:
        print("Not a number integer")
        return False

def get_status_tank(quantity):
    if quantity <= 1:
        print(f"{quantity}% <E>")
    elif quantity >= 99:
        print(f"{quantity}% <F>")
    else:
        print(f"Tank: {quantity}%") 

main()