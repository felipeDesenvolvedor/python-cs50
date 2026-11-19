import sys
import re

def main():
   print(shorten(input("Input: ")))

def shorten(tweets): 
    newTwttr = re.findall("([^aeiouAEIOU]+)", tweets)
    newTwttr = "".join(newTwttr)
    newVowel = re.findall("([aeiouAEIOU]+)", newTwttr)

    if len(newVowel) > 0:
        sys.exit(1)

    return "".join(newTwttr)

if __name__ == "__main__":
    main()