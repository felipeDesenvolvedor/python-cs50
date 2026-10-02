for i in range(3):
    with open("names.txt", "a") as file:
        file.write(f"{input("What's your name? ")}\n")

with open("names.txt", "r") as file:
    for line in sorted(file.readlines()):
        print("hello", line.strip())