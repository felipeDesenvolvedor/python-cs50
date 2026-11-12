import re

def main():
    is_valid_plate(input("Plate: "))


def is_valid_plate(plate):
    if is_valid(plate.strip()):
        print("Valid")
        return "Valid"
    else:
        print("Invalid")
        return "Invalid"

def is_valid(s):
    
    if valid_leng_plate(s):
        return first_second_caract_alpha(s) and valid_format_plate(s)

def first_second_caract_alpha(s):
    return s[0].isalpha() and s[1].isalpha()

def valid_leng_plate(s):
    return len(s) >= 2 and len(s) <= 6

def valid_format_plate(s):

    if (re.search(r"^([a-zA-Z]+)([^0])([0-9]+)$", s) and not is_firs_caract_zero(s)) or is_not_content_number(s):
        return True

    return False

def is_firs_caract_zero(s):
    for c in s:
        if c.isnumeric():
            return c == "0"

    return False

def is_not_content_number(s):
    return s.isalpha()

if __name__ == "__main__":
    main()
