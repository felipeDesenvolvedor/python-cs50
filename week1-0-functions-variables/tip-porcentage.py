def main():
    try:
        dollars = dollars_to_float(input("How much was the meal? "))
        percent = percent_to_float(input("What percentage would you like to tip? "))
        tip = dollars * percent
        print(f"Leave ${tip:.2f}")
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
    
main()