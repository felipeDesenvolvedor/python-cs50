def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    print(valid_format_plate(s))
    if valid_leng_plate(s):
        return valid_first_second_caract(s)

def valid_first_second_caract(s):
    return s[0].isalpha() and s[1].isalpha()

def valid_leng_plate(s):
    return len(s) >= 2 and len(s) <= 6

def valid_format_plate(s):
    firs_caract_zero = s.startswith("0")
    last_caract_alfa = s[len(s) - 1].isalpha()
    return firs_caract_zero or last_caract_alfa

main()