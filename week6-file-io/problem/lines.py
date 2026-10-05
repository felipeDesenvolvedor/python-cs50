import sys
# (OK) o nome (ou caminho) de um arquivo Python, e exibe o número de linhas de código nesse arquivo, excluindo comentários e linhas em branco.
# (OK) Se o usuário não especificar exatamente um argumento de linha de comando, ou se o nome do arquivo especificado não terminar em .py, ou se o arquivo especificado não existir, o programa deverá ser encerrado com um erro sys.exit
# () Considere que qualquer linha que comece com `\n` #, opcionalmente precedida por um espaço em branco, é um comentário. (Uma docstring não deve ser considerada um comentário.) 
# () Considere que qualquer linha que contenha apenas espaços em branco está em branco.

def main():
    if(is_file_valid(sys.argv)):
        count_lines(sys.argv[1])

def is_file_valid(args):
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    if len(args) > 2:
        sys.exit("Too many command-line arguments")
    if not args[1].endswith(".py"):
        sys.exit("Not a Python file")

    return True

def count_lines(file_name):
    number_of_lines = 0

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                if is_comment(line) or is_blank(line) or is_docstring(line):
                    continue
                number_of_lines += 1
        print(number_of_lines)    
    except FileNotFoundError:
        sys.exit("File does not exist")

def is_comment(line):
    return line.strip().startswith('#')
def is_blank(line):
    return line.strip() == ""

def is_docstring(line):
    return line.strip().startswith('"""') or line.strip().startswith("'''")

""" def is_docstring(line):
    return line.strip().startswith('"""') or line.strip().startswith("'''") """

if __name__ == "__main__":
    main()