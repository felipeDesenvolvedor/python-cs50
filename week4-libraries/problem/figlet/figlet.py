

import sys
from pyfiglet import Figlet

def main():
    print(get_text_font(input("Input: ")))

def get_text_font(text):

    try:
        if len(sys.argv) == 1:
            return get_font_random(text)

        if (len(sys.argv) == 3) and sys.argv[1] != "-f" and sys.argv[1] != "--font":
                raise ValueError(f"Invalid usage") 
        
        if len(sys.argv) == 3:
            return get_font_specific(text, sys.argv[2])
            
    except Exception as e:
        return str(e)

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