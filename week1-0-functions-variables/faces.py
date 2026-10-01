def main():
    get_message()


def get_message():
    message = input("Insira sua mensagem: ")
    print(convert(message))


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
main()    
