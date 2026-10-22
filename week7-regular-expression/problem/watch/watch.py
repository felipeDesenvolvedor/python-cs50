import re

def main():
    print(parse(input("HTML: ")))
   
def parse(textUrl):
    matches = re.search(r'^<iframe.*src=("[^"]+").*></iframe>$', textUrl, re.IGNORECASE)
    return str(matches.group(1))

if __name__ == "__main__":
    main()