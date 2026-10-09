"""
1) As classes são uma forma pela qual, na programação orientada a objetos, podemos inventar nosso próprio tipo de dado e dar-lhe um nome — como um molde para um tipo de dado.
2) Podemos modificar nosso código da seguinte forma para implementar nossa própria classe chamada Student:
3) Observe que, por convenção, a primeira letra Studenté maiúscula. Além disso, note que o `\n` ...simplesmente significa que retornaremos mais tarde para concluir essa parte do nosso código. Observe também que, em `\n` get_student, podemos criar uma studentvariável da classe ` \n` Studentusando a sintaxe `\n` student = Student(). Observe ainda que utilizamos a notação de ponto para acessar os atributos dessa variável studentda classe `\n` Student.
4) Sempre que você cria uma classe e utiliza esse modelo para criar algo, você cria o que é chamado de "objeto" ou "instância". No caso do nosso código, ` studentis` é um objeto.
5) Observe que Student, dentro de `Class`, padronizamos os atributos dessa classe. Podemos criar uma função dentro de `Class` class Student, chamada de "método", que determina o comportamento de um objeto da classe `Object` Student. Dentro dessa função, ela recebe `value` namee house`value` como parâmetros e atribui essas variáveis ​​a esse objeto. Além disso, observe como o construtor student = Student(name, house)chama essa função dentro da Studentclasse e cria um `Object` student. self`object` se refere ao objeto atual que acabou de ser criado.
6) A programação orientada a objetos incentiva você a encapsular toda a funcionalidade de uma classe dentro da definição da classe. E se algo der errado? E se alguém tentar digitar algo aleatório? E se alguém tentar criar um aluno sem nome? Modifique seu código da seguinte forma:
7) Observe como agora verificamos se um nome foi fornecido e se uma casa adequada foi designada. Descobrimos que podemos gerar nossas próprias exceções usando `Exception` raise, alertando o programador sobre um possível erro cometido pelo usuário. No caso acima, geramos uma exceção ValueErrorcom uma mensagem de erro específica.
8) Observe como o def __str__(self)método `print` fornece um meio de retornar uma representação em string do aluno quando o objeto é impresso. Portanto, agora você pode, como programador, imprimir um objeto, seus atributos ou praticamente qualquer coisa que desejar relacionada a esse objeto.
9) __str__ é um método integrado que vem com as classes do Python. Acontece que também podemos criar nossos próprios métodos para uma classe! Modifique seu código da seguinte forma:

Decorators
1) As propriedades podem ser utilizadas para reforçar a segurança do nosso código. Em Python, definimos propriedades usando "decoradores" de função, que começam com `properties` @. Modifique seu código da seguinte forma:
2) Observe como escrevemos @propertyacima uma função chamada ` house. Isso define `house` housecomo uma propriedade da nossa classe. Com ` househouse` como propriedade, ganhamos a capacidade de definir como algum atributo da nossa classe, ` _househouse`, deve ser definido e recuperado. De fato, agora podemos definir uma função chamada "setter", por meio de `.` @house.setter, que será chamada sempre que a propriedade `house` for definida — por exemplo, com student.house = "Gryffindor"`. Aqui, fizemos com que nosso setter validasse os valores de `house` housepara nós. Observe como lançamos uma exceção ValueErrorse o valor de `house` housenão for nenhuma das casas de Harry Potter; caso contrário, usaremos `.` housepara atualizar o valor de `house` _house. Por que `.` _housee não house`.`? house`house` é uma propriedade da nossa classe, com funções por meio das quais um usuário tenta definir nosso atributo de classe. _house`house` é o próprio atributo de classe. O sublinhado inicial, ` __`, indica aos usuários que eles não precisam (e, de fato, não devem!) modificar esse valor diretamente. `house` só_house deve ser definido por meio do setter. Observe como a propriedade simplesmente retorna o valor de `house` , nosso atributo de classe que presumivelmente foi validado usando nosso setter. Quando um usuário chama `.` , ele está obtendo o valor de `house` por meio do nosso "getter".househouse_househousestudent.house_househouse
3) Observe como, assim como no código anterior, fornecemos um getter e um setter para o nome.
4) Observe que o método ` get_studentis` foi removido e um @classmethodmétodo chamado ` getis` foi criado. Agora, esse método pode ser chamado sem a necessidade de criar um aluno primeiro.

Métodos Estáticos
1) Descobriu-se que, além dos @classmethod métodos `s`, que são distintos dos métodos de instância, existem também outros tipos de métodos.
2) O uso de métodos estáticos @staticmethod pode ser algo que você queira explorar. Embora não seja abordado explicitamente neste curso, você pode pesquisar e aprender mais sobre métodos estáticos e sua distinção em relação aos métodos de classe.

"""

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter for house
    @property
    def house(self):
        return self._house

    # Setter for house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()