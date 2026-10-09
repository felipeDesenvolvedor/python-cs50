"""
    Podemos simplificar ainda mais nosso programa armazenando o aluno como uma sequência de valores. Ao contrário de um número inteiro tuple, uma sequência de valores não pode ser modificada. Na prática, estamos retornando dois valores.tuple list tuple
    Empacotando isso tuple, de forma que possamos retornar ambos os itens para uma variável chamada student, podemos modificar nosso código da seguinte maneira:
    tuple Os valores são imutáveis, o que significa que não podemos alterá-los. A imutabilidade é uma forma de programarmos de forma defensiva.
    Observe que este código produz um erro. Como tupleos valores de `s` são imutáveis, não podemos reatribuir o valor de `s` student[1].
"""
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()