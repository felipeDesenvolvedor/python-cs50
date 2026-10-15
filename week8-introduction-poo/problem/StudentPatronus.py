"""
1) As classes são uma forma pela qual, na programação orientada a objetos, podemos inventar nosso próprio tipo de dado e dar-lhe um nome — como um molde para um tipo de dado.
2) Podemos modificar nosso código da seguinte forma para implementar nossa própria classe chamada StudentPatronus:
3) Observe que, por convenção, a primeira letra Studenté maiúscula. Além disso, note que o `\n` ...simplesmente significa que retornaremos mais tarde para concluir essa parte do nosso código. Observe também que, em `\n` get_student, podemos criar uma studentvariável da classe ` \n` Studentusando a sintaxe `\n` student = StudentPatronus(). Observe ainda que utilizamos a notação de ponto para acessar os atributos dessa variável studentda classe `\n` StudentPatronus.
4) Sempre que você cria uma classe e utiliza esse modelo para criar algo, você cria o que é chamado de "objeto" ou "instância". No caso do nosso código, ` studentis` é um objeto.
5) Observe que StudentPatronus, dentro de `Class`, padronizamos os atributos dessa classe. Podemos criar uma função dentro de `Class` class StudentPatronus, chamada de "método", que determina o comportamento de um objeto da classe `Object` StudentPatronus. Dentro dessa função, ela recebe `value` namee house`value` como parâmetros e atribui essas variáveis ​​a esse objeto. Além disso, observe como o construtor student = StudentPatronus(name, house)chama essa função dentro da Studentclasse e cria um `Object` student. self`object` se refere ao objeto atual que acabou de ser criado.
6) A programação orientada a objetos incentiva você a encapsular toda a funcionalidade de uma classe dentro da definição da classe. E se algo der errado? E se alguém tentar digitar algo aleatório? E se alguém tentar criar um aluno sem nome? Modifique seu código da seguinte forma:
7) Observe como agora verificamos se um nome foi fornecido e se uma casa adequada foi designada. Descobrimos que podemos gerar nossas próprias exceções usando `Exception` raise, alertando o programador sobre um possível erro cometido pelo usuário. No caso acima, geramos uma exceção ValueErrorcom uma mensagem de erro específica.
8) Observe como o def __str__(self)método `print` fornece um meio de retornar uma representação em string do aluno quando o objeto é impresso. Portanto, agora você pode, como programador, imprimir um objeto, seus atributos ou praticamente qualquer coisa que desejar relacionada a esse objeto.
9) __str__ é um método integrado que vem com as classes do Python. Acontece que também podemos criar nossos próprios métodos para uma classe! Modifique seu código da seguinte forma:
10) 
"""

class StudentPatronus:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return StudentPatronus(name, house, patronus)


if __name__ == "__main__":
    main()