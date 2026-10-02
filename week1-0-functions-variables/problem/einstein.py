def main():
    get_joules(int(input("Digite a M: ")))


def get_joules(mass):
    try:
        speed = 300000000
        speedSquare = speed * speed
        joules = mass * speedSquare
        print("E: ", joules)
        return joules
    except ValueError as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()