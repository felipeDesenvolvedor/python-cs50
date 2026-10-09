# Conexão com trabalhos anteriores neste curso
# Embora não tenha sido explicitamente mencionado em partes anteriores deste curso, você esteve utilizando classes e objetos durante todo o processo.
# Se você analisar a documentação de `std::string` int, verá que se trata de uma classe com um construtor. É um modelo para criar objetos do tipo `std::string` int. Você pode aprender mais na documentação de `std::string` do Python int.
# Strings também são uma classe. Se você usou `string` str.lower(), estava usando um método que pertence à strclasse. Você pode aprender mais na documentação do Python sobre strings str.
# listtambém é uma classe. Consultando a documentação de list, você pode ver os métodos que ela contém, como list.append(). Você pode aprender mais na documentação de do Python list.
# dictTambém é uma classe dentro do Python. Você pode aprender mais na documentação do Python sobre dict.
#
# 
# 1) Para ver como você tem usado classes o tempo todo, vá ao seu terminal e digite code type.pyo seguinte código:
# Observe como, ao executar este código, será exibido que a classe de 50 é int.
print(type(50))

# 2) Também podemos aplicar isso da str seguinte forma:
# Observe como a execução deste código indicará que ele pertence à classe str.
print(type("hello, world"))

print(type([]))

print(type(list()))

print(type({}))

print(type(dict()))