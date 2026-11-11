import re

def main():
    is_valid(input("Plate: "))


def is_valid(plate):
    if is_valid_format(plate):
        print("Valid")
        return True
    else:
        print("Invalid")
        return False

def is_valid_format(s):
    
    if valid_leng_plate(s):
        return first_second_caract_alpha(s) and valid_format_plate(s)

def first_second_caract_alpha(s):
    return s[0].isalpha() and s[1].isalpha()

def valid_leng_plate(s):
    return len(s) >= 2 and len(s) <= 6

def valid_format_plate(s):
    last_caract_alfa = s[len(s) - 1].isalpha()

    valid_format = (not is_firs_caract_zero(s)) and (not last_caract_alfa) and (not is_valid_caracteres_special(s))
    return valid_format

def is_firs_caract_zero(s):
    for c in s:
        if c.isnumeric():
            return c == "0"

    return False

def is_valid_caracteres_special(s):
    padrao = r'[^a-zA-Z0-9\s]'
    especiais = re.findall(padrao, s)
    return len(especiais) > 0
    

if __name__ == "__main__":
    main()
