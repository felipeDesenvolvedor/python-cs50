def main():
   print(get_calories(input("Enter fruit name: ")))


def get_calories(name):
    fruit = name.lower().strip()
    fruit = fruit.split(" ")
    fruit = "".join(fruit).lower()

    fruits = [
        {"name": "apple", "calories": 130},
        {"name": "avocado", "calories": 50},
        {"name": "banana", "calories": 110},
        {"name": "cantaloupe", "calories": 50},
        {"name": "grapefruit", "calories": 60},
        {"name": "grapes", "calories": 90},
        {"name": "sweetcherries", "calories": 100},
        {"name": "kiwifruit", "calories": 90},
        {"name": "pear", "calories": 100}
    ]

    for f in fruits:
        if f["name"] == fruit:
            return "Calories: " + str(f["calories"])

    return ''
if __name__ == "__main__":
    main()
