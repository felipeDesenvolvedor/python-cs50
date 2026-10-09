# Às vezes, queremos adicionar funcionalidades à própria classe, e não às instâncias dessa classe.
# @classmethod É um decorador que podemos usar para adicionar funcionalidades a uma classe como um todo.
# No entanto, podemos querer executar a sortfunção sem criar uma instância específica do chapéu seletor (afinal, só existe um!). Podemos modificar nosso código da seguinte forma:
# Observe como o __init__método é removido porque não precisamos instanciar um `hat` em nenhum lugar do nosso código. selfPortanto, ele não é mais relevante e é removido. Especificamos isso sortcomo um `hat` @classmethod, substituindo self-o por `hat` cls. Finalmente, observe como ` Hathat` é maiúsculo por convenção perto do final deste código, porque este é o nome da nossa classe.

import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")