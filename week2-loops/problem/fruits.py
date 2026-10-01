def main():
   print(get_calories(input("Enter fruit name: ")))


def get_calories(name):
    fruit = name.lower()
    fruit = fruit.split(" ")
    fruit = "".join(fruit).lower()

    fruits = [
        {"name": "apple", "calories": 130, "portion": 242},
        {"name": "avocado", "calories": 50, "portion": 30},
        {"name": "banana", "calories": 110, "portion": 126 },
        {"name": "cantaloupe", "calories": 50, "portion": 134 },
        {"name": "grapefruit", "calories": 60, "portion": 154 },
        {"name": "grapes", "calories": 90, "portion": 126 },
        {"name": "sweetcherries", "calories": 100, "portion": 30 }
    ]

    for f in fruits:
        if f["name"] == fruit:
            return "Portion: " + str(f["portion"]) + " gm = " + "Calories " + str(f["calories"])

if __name__ == "__main__":
    main()
