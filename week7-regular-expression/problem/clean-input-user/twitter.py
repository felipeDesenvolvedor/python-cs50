import re
# As expressões regulares simplesmente nos permitem expressar os padrões e objetivos de forma sucinta.

def main():
    url = input("URL: ").strip()

    # username = url.removeprefix("https://twitter.com/")
    # print(f"Username: {username}")
    # username = url.replace("https://twitter.com/", "")
    # print(f"Username: {username}")

    if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
        print(f"Username:", matches.group(1))

if __name__ == "__main__":
    main()