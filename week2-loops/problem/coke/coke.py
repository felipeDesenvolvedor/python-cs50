def main():
    get_values()


def get_values():
    koin1 = 5
    koin2 = 10
    koin3 = 25
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        pay = int(input("Insert Coin: "))
        if koin1 == pay or koin2 == pay or koin3 == pay:
            amount_due = amount_due - pay

    print(f"Change Owed: {abs(amount_due)}")

main()