import re

def main():
    name = input("What's your name? ").strip()
    if matches := re.search(r"^(.+), *(.+)$", name):
        """
         Observe como combinamos duas linhas do nosso código. O :=operador morsa atribui um valor da direita para a esquerda e nos permite fazer uma pergunta booleana ao mesmo tempo. Vire a cabeça para o lado e você entenderá por que isso é chamado de operador morsa.
        """
        name = matches.group(2) + " " + matches.group(1)
    print(f"hello, {name}")

if __name__ == "__main__":
    main()