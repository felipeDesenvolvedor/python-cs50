def main():
    get_itens()

def get_itens():
    optionsItens = {
        "bajataco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "superburrito": 8.50,
        "superquesadilla": 9.50,
        "taco": 3.00,
        "tortillasalad": 8.00
    }
    total_itens = 0

    while True:
        try:
            try:
                item = input("Item:").split(" ")
                item = "".join(item).lower()
                total_itens += optionsItens[item]
                print(f"Total: ${total_itens:.2f}")

            except EOFError:
                break
        except Exception as e:
            print("An error occurred:", e)

main()