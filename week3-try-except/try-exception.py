# Requisitos dos exemplos e exercicios
# Criar um programa que peça um numero inteiro
# Realizar o tratamento de erros usando try exception para validar se o usuario digitou mesmo numero inteiro
# Criar uma rotina repetir o pedido do numero inteiro caso algo de errado e o numero não seja capturado

def main():
    get_int("Digite um numero inteiro: ")


def get_int(message):
    while True:
        try:
            valor = int(input(message))
            break
        except:
            print("Não é um numero inteiro")
    print(valor)

main()
