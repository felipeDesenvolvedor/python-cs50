import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
   try:
       if re.search(r"^(\d{1,2}?)(:\d{1,2}?)? (AM|PM) to (\d{1,2}?)(:\d{1,2}?)? (PM|AM)$", s):
           print("Valid")
           return "Valid"
       else:
           raise ValueError("Invalid")  
   except ValueError as e:
       print(e)
       return e
       

if __name__ == "__main__":
    main()