def main():
    print(interpreterExpresion(input("Expression: ")))

def interpreterExpresion(expresion):
    numero1 = expresion.strip().split(" ")[0]
    operador = expresion.strip().split(" ")[1]
    numero2 = expresion.strip().split(" ")[2]

    if operador == "+":
        return f"{round(float(int(numero1) + int(numero2)), 1)}"
    
    if operador == "-":
        return f"{round(float(int(numero1) - int(numero2)), 1)}"
    
    if operador == "*":
        return f"{round(float(int(numero1) * int(numero2)), 1)}"
    
    if operador == "/":
        return f"{round(float(int(numero1) / int(numero2)), 1)}"

if __name__ == "__main__":
    main()