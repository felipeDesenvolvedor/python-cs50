import os
import sys

from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    fileNameOne = sys.argv[1]
    fileNameTwo = sys.argv[2]
    check_extension(fileNameOne, fileNameTwo)

    shirt_path = os.path.join(os.path.dirname(__file__), "shirt.png")
    try:
        image = Image.open(fileNameOne)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    with image:
        with Image.open(shirt_path) as shirt:
            photo = ImageOps.fit(image, shirt.size)
            photo.paste(shirt, shirt)
            photo.save(fileNameTwo)


def check_extension(fileNameOne, fileNameTwo):
    input_extension = os.path.splitext(fileNameOne)[1].lower()
    output_extension = os.path.splitext(fileNameTwo)[1].lower()
    valid_extensions = {".jpg", ".jpeg", ".png"}

    if input_extension not in valid_extensions:
        sys.exit("Invalid input")
    if output_extension not in valid_extensions:
        sys.exit("Invalid output")
    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()