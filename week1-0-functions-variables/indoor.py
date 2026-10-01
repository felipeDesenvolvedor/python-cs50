def main():
    get_str(input("Escreva sua mensagem: "))


def get_str(m):
    message = m.lower()
    print("O usuário disse", message)
    return message


if __name__ == "__main__":
    main()