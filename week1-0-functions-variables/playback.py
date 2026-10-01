def main():
    get_audio(input("Insira sua fala: "))


def get_audio(audio):
    words = audio.split(" ")
    words = "...".join(words)
    print(words)
    return words


if __name__ == "__main__":
    main()