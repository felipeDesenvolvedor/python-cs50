from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self._title_shirt = ""
        self._name = ""

    @property
    def title_shirt(self):
        return self._title_shirt

    @title_shirt.setter
    def title_shirt(self, title):
        self._title_shirt = title
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing titleShirt:
        self.cell(None, 10, self.title_shirt, border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def chapter_body(self):
        # Setting font: Times 12
        self.set_font("Times", size=18)
        self.set_text_color(225, 225, 225)
        self.set_y(self.y / 2)
        self.cell(self.w, 5, f"{self.name} took CS50", align="C")

    def print_chapter(self, title, name):
        imgPath = "https://cs50.harvard.edu/python/psets/8/shirtificate/shirtificate.png"
        self.title_shirt = title
        self.name = name
        self.set_margin(0)
        self.set_top_margin(5)
        self.add_page()
        self.image(imgPath, "CENTER")
        self.chapter_body()
        self.output("shirtificate.pdf")
        
