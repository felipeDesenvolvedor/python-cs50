def main():
    nameVariable = input("camelCase: ")
    nameVariabelSnackCase = []

    for c in nameVariable:
        if c.isupper():
            nameVariabelSnackCase.append("_"+c.lower())
        else:
            nameVariabelSnackCase.append(c)
    

    print("snake_case: ", "".join(nameVariabelSnackCase))
main()