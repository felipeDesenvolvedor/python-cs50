def main():
    get_message(input("Insira sua mensagem: "))


def get_message(m):
    messageReturn = convert(m)
    print(messageReturn)
    return messageReturn


def convert(message):
    try:
        emojis = {":}":"😀", ":)":"😂", ":fogo":"🔥", ":joinha":"👍", ":heart":"❤️", ":rocket":"🚀", ":sparkles":"✨", ":sunglasses":"😎", ":(":"☹️"}
        caracteres = message.split(" ")
        newCaracteres = []
        for i in caracteres:
            if emojis.get(i):
                newCaracteres.append(emojis.get(i))
            else:
                newCaracteres.append(i)

        return " ".join(newCaracteres)
    except KeyError as e:
        print("Erro", e)


if __name__ == "__main__":
    main()    
