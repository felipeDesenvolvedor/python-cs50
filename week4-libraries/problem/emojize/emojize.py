import emoji

def main():
    print(get_emoji(input("Input: ")))

def get_emoji(emoji_alias = ":thumbsup:"):
    return emoji.emojize(f"Python is {emoji_alias}", language='alias')

if __name__ == "__main__":
    main()