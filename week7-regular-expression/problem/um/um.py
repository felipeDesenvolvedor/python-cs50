import re

def main():
    print(count(input("Text: ")))

def count(s):
    quantityUm = re.findall(r'\b(um|Um)\b', s, re.IGNORECASE)
    return len(quantityUm)

if __name__ == "__main__":
    main()