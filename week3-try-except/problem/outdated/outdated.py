import datetime

def main():
    while True:
        try:
            date_input = input("Date: ")
            if not date_input:
                break
            print(convert_outdated(date_input))
            break
        except ValueError as e:
            print(f"Error: {e}")

def convert_outdated(dateOutdated):
    try:
        if dateOutdated.count("/"):
            return f'{datetime.date.strptime(dateOutdated, "%m/%d/%Y")}'
        else:
            return f'{datetime.date.strptime(dateOutdated, "%B %d, %Y")}'
    except ValueError as e:
        raise ValueError(f"Error: {e}")

if __name__ == "__main__":
    main()