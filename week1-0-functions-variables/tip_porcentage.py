def main():
    get_percentage(input("How much was the meal? "), input("What percentage would you like to tip? "))


def get_percentage(dollars, percent):
    try:
        dollars = dollars_to_float(dollars)
        percent = percent_to_float(percent)
        tip = dollars * percent
        print(f"Leave ${tip:.2f}")
        return f"Leave ${tip:.2f}"
    except ValueError as e:
        print(e)

def dollars_to_float(d):
    valueMeal = d.split("$")
    valueMeal = valueMeal[1]
    return float(valueMeal)

def percent_to_float(p):
    percent = p.split("%")
    percent = percent[0]
    return float(percent) / 100

if __name__ == "__main__":    
    main()