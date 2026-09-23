def main():
    get_mass()


def get_mass():
    try:
        speed = 300000000
        speedSquare = speed * speed
        mass = int(input("Digite a M: "))
        joules = mass * speedSquare
        print("E: ", joules)
    except ValueError as e:
        print("An error occurred:", e)

main()