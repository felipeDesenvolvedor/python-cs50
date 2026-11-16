

import sys
from pyfiglet import Figlet

def main():
    font = get_font()
    print(get_text_font(input("Input: "), font))


def get_font():
    if len(sys.argv) == 1:
        return None

    if len(sys.argv) != 3 or sys.argv[1] not in ("-f", "--font"):
        sys.exit(1)

    font = sys.argv[2]
    if font not in Figlet().getFonts():
        sys.exit(1)
    return font


def get_text_font(text, font=None):
    if font is None:
        return get_font_random(text)
    return get_font_specific(text, font)

def get_font_random(message="Hello, World!"):
    try:
        figlet = Figlet()
        figlet.getFonts()
        figlet.setFont(font="slant")
        return figlet.renderText(message)
    except Exception as e:
        raise ValueError(f"Invalid usage")

def get_font_specific(message="Hello, World!", font="slant"):
    try:
        figlet = Figlet()
        figlet.getFonts()
        figlet.setFont(font=font)
        return figlet.renderText(message)
    except Exception as e:
        raise ValueError(f"Invalid usage")

if __name__ == "__main__":
    main()