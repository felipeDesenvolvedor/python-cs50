def main():
    get_audio()


def get_audio():
    audio = input("Insira sua fala: ")
    words = audio.split(" ")
    print("..".join(words))

main()