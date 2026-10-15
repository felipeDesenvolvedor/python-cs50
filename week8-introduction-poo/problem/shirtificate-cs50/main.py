# 1) OK - A orientação do PDF deve ser Retrato.
# 2) OK - O formato do PDF deve ser A4, que tem 210 mm de largura por 297 mm de altura.
# 3) OK - O topo do PDF deve conter o texto “CS50 Shirtificate” , centralizado horizontalmente.
# 4) OK - A imagem da camisa deve estar centralizada horizontalmente.
# 5) O nome do usuário deve estar na parte superior da camisa, em letras brancas.
# 

from shirtificate import PDF

def main():
    pdf = PDF()
    name = input("Name: ")
    pdf.print_chapter("CS50 Shirtificate", name)

if __name__ == "__main__":
    main()
