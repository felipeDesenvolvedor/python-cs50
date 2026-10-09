# () Em um arquivo chamado pizza.py, implemente um programa que espera exatamente um argumento de linha de comando, o nome (ou caminho) de um arquivo CSV no formato Pinocchio
# () gera uma tabela formatada como arte ASCII usando tabulate, um pacote disponível no PyPI em pypi.org/project/tabulate 
# () Formate a tabela usando o gridformato da biblioteca.  
# () Se o usuário não especificar exatamente um argumento de linha de comando, ou se o nome do arquivo especificado não terminar em .csv, ou se o arquivo especificado não existir, o programa deve ser encerrado com um erro sys.exit.


import sys
import csv
from tabulate import tabulate

def main():
    if(is_file_valid(sys.argv)):
            mount_table(sys.argv[1])

def is_file_valid(args):
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    if len(args) > 2:
        sys.exit("Too many command-line arguments")
    if not args[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    return True

def mount_table(file_name):
    try:
        with open(file_name, "r") as file:
            lines = csv.DictReader(file)
            table = []
            headers = list(lines.fieldnames)
            for line in lines:
                table.append(list(line.values()))
            print(tabulate(table, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()