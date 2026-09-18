# Os indicadores de combustível mostram, geralmente com frações, a quantidade exata de combustível no tanque. Por exemplo, 1/4 indica que o tanque está 25% cheio, 1/2 indica que o tanque está 50% cheio e 3/4 indica que o tanque está 75% cheio.
# Em um arquivo chamado fuel.py, implemente um programa que solicite ao usuário uma fração, formatada como X/Y, onde Xé um inteiro não negativo e Yé um inteiro positivo, e então imprima, como uma porcentagem arredondada para o inteiro mais próximo, a quantidade de combustível restante no tanque. Se, no entanto, restar 1% ou menos, imprima Epara indicar que o tanque está praticamente vazio. E se restar 99% ou mais, imprima Fpara indicar que o tanque está praticamente cheio.
# Se, no entanto, X`n` Ynão for um número inteiro, Xfor maior que `n` Y, ou Yfor `n` 0, solicite novamente ao usuário. (Não é necessário que ` Yn` seja `n` 4.) Certifique-se de capturar quaisquer exceções como `NULL` ValueErrorou `NULL`

# Requisitos
# OK) Em um arquivo chamado fuel.py, implemente um programa que solicite ao usuário uma fração, formatada como X/Y
# OK) X é um inteiro não negativo e Y é um inteiro positivo
# 3) então imprima, como uma porcentagem arredondada para o inteiro mais próximo, a quantidade de combustível restante no tanque.
# 4) Se, no entanto, restar 1% ou menos, imprima E
# 5) se restar 99% ou mais, imprima F para indicar que o tanque está praticamente cheio.
# 6) Se, no entanto, X `n` Y não for um número inteiro, X for maior que `n` Y, ou Y for `n` 0, solicite novamente ao usuário.
# 6) Certifique-se de capturar quaisquer exceções como `NULL` ValueErrorou `NULL` Zero DivisionError.

def main():
    get_fractions()

def get_fractions():
    while True:
        fraction = input("Fraction: ")
        numerador = get_parts_fractions(fraction)["numerador"]
        denominador = get_parts_fractions(fraction)["denominador"]

        if(chekPositiveNumbers(numerador, denominador)):
            get_porcentage(numerador, denominador)
            break

def get_porcentage(numerador, denominador):
    print(int((int(numerador) / int(denominador)) * 100), "%")   

def get_parts_fractions(param):
    return {"numerador":param.split("/")[0], "denominador":param.split("/")[1]}

def chekPositiveNumbers(numerador, denominador):
    return int(numerador) < int(denominador) and int(numerador) > 0

main()