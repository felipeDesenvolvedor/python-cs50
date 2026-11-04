from PIL import Image
import sys

def main():
    shirt()

def shirt():
    try:

        if len(sys.argv) <= 2:
            raise ValueError("Too few command-line arguments")
        
        fileNameOne = sys.argv[1]
        fileNameTwo = sys.argv[2]

        if check_extension(fileNameOne, fileNameTwo):
            print("Success: Both file names have the same extension.")
    except ValueError as e:
        print(e)
        return e
        sys.exit(1)

def check_extension(fileNameOne, fileNameTwo):

    if ".jpeg" in fileNameOne or ".jpg" in fileNameOne or ".png" in fileNameOne:
        pass
    else:
        raise ValueError("Invalid input")

    if ".jpeg" in fileNameTwo or ".jpg" in fileNameTwo or ".png" in fileNameTwo:
        pass
    else:
        raise ValueError("Invalid output")

    if fileNameOne.split(".")[1] != fileNameTwo.split(".")[1]:
        raise ValueError("Input and output have different extensions.")

    return True

if __name__ == "__main__":
    main()