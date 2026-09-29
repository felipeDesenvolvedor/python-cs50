def main():
     get_snack_case(input("camelCase: "))


def get_snack_case(string):
     nameVariable = string
     nameVariabelSnackCase = []

     for c in nameVariable:
        if c.isupper():
            nameVariabelSnackCase.append("_"+c.lower())
        else:
            nameVariabelSnackCase.append(c)
    
     print("snake_case: ", "".join(nameVariabelSnackCase))
     return "".join(nameVariabelSnackCase)

if __name__ == "__main__":
    main()