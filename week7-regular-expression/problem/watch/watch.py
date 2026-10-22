import re

def main():
    print(parse(input("HTML: ")))
   
def parse(textUrl):
    matches = re.search(r'^<iframe.*src=("https?://(www\.)?youtube.com/embed/[^"]+").*></iframe>$', textUrl, re.IGNORECASE)

    if matches:
        return str(matches.group(1))
    else:
        return None

if __name__ == "__main__":
    main()