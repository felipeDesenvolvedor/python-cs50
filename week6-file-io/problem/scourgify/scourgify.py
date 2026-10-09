import sys
import csv

def main():
    if(is_file_valid(sys.argv)):
        transform_files(sys.argv[1], sys.argv[2])

def is_file_valid(args):
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    if len(args) > 3:
        sys.exit("Too many command-line arguments")
    if not args[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    return True

def transform_files(file_source, file_destination):
    try:
        with open(file_source, "r") as source_file:
            with open(file_destination, "w") as destination_file:
                reader = csv.DictReader(source_file)
                writer = csv.DictWriter(destination_file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    writer.writerow(transform_columns(row))
    except FileNotFoundError:
        sys.exit(f"Could not read {file_source}")

def transform_columns(row):
    first = row["name"].split(",")[1].strip()
    last = row["name"].split(",")[0].strip()
    house = row["house"].strip()

    return {"first": first, "last": last, "house": house}

if __name__ == "__main__":
    main()