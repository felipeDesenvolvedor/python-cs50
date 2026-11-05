import inflect
p = inflect.engine()

def main():
    print(adieu())

def adieu():
    names = []
    message = "Adieu, adieu, to"

    while True:
        try:
            names.append(input("Name: "))
        except EOFError as e:
            break

    return f"\n{message} {p.join(names)}"

if __name__ == "__main__":
    main() 