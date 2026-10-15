"""
Herança

1) A herança é, talvez, a característica mais poderosa da programação orientada a objetos.
2) Acontece que você pode criar uma classe que "herda" métodos, variáveis ​​e atributos de outra classe.
3) No terminal, execute code wizard.pyo seguinte código:

Herança e Exceções
1) Embora tenhamos acabado de introduzir a herança, já a vínhamos utilizando há muito tempo em nosso uso de exceções.
2) Acontece que as exceções ocorrem em uma hierarquia, onde existem classes filhas, pais e avós. Estas são ilustradas abaixo:

BaseException
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- KeyError
      +-- NameError
      +-- SyntaxError
      |    +-- IndentationError
      +-- ValueError
 ...

Resumindo
    Agora, você aprendeu um nível totalmente novo de capacidade através da programação orientada a objetos.
    
    1 Programação orientada a objetos
    2 Aulas
    3 raise
    4 Decoradores
    5 Métodos de classe
    6 Métodos Estáticos
    7 Herança
    8 Sobrecarga do operador   
"""

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def __str__(self):
        return f"{self.name}"

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{self.name} teaches {self.subject}"


def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense Against the Dark Arts")

    print(wizard)
    print(student)
    print(professor)

if __name__ == "__main__":
    main()