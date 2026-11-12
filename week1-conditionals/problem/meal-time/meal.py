def main():
    print(convert(input("What time is it? ")))

def convert(time):
    hour, minutes = time.strip().split(":")

    if(int(minutes) >= 60):
        raise ValueError("Invalid minutes")

    if int(hour) == 7 and int(minutes) >= 0 and int(minutes) <= 59 or int(hour) == 8:
        return "breakfast time"
    
    if int(hour) == 12 and int(minutes) >= 0 and int(minutes) <= 59 or int(hour) == 13:
        return "lunch time"
    
    if int(hour) == 18 and int(minutes) >= 0 and int(minutes) <= 59 or int(hour) == 19:
        return "dinner time"

if __name__ == "__main__":
    main()