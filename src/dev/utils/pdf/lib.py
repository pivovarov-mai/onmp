from fpdf import FPDF


class MDoc(object):
    def __init__(self):
        self.left = 17
        self.top = 20
        self.right = 12
        self.bottom = 15
        self.page_limit = 209 - self.right
        self.pdf = FPDF()
        self.pdf.add_font("DejaVu-Bold", "", "DejaVuSansCondensed-Bold.ttf", uni=True)
        self.pdf.add_font("DejaVu", "", "DejaVuSansCondensed.ttf", uni=True)

    def ln(self):
        self.pdf.ln(4)

    def set_margins(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.page_limit = 209 - self.right

    def create(self):
        self.pdf.set_margins(self.left, self.top, self.right)
        self.pdf.set_auto_page_break(True, self.bottom)
        self.pdf.add_page()

    def pline(self):
        x1 = self.pdf.get_x() + 1
        y = self.pdf.get_y() + 2
        self.pdf.line(x1, y, self.page_limit, y)

    def dynamic_pole(self, title, subtitle, text):
        self.pdf.set_font("DejaVu-Bold", "", 9)
        self.pdf.write(2, title)
        self.pdf.set_font("DejaVu", "", 7)
        self.pdf.write(2, subtitle + " ")
        x = self.pdf.get_x()
        y = self.pdf.get_y()
        self.pdf.set_xy(self.pdf.get_x(), self.pdf.get_y() - 1)
        self.pdf.write(4, text)
        cur_x = self.pdf.get_x()
        cur_y = self.pdf.get_y()
        for i in range((int)((self.pdf.get_y() - y) / 3) - 1):
            self.pdf.set_xy(17, y + 3 * (i + 1) + i + 1)
            self.pline()
        if (int)((self.pdf.get_y() - y) / 3) - 1 == 0 and y != cur_y:
            self.pdf.set_xy(17, cur_y + 1)
            self.pline()
        self.pdf.set_xy(x, y)
        self.pline()
        self.pdf.set_xy(cur_x, cur_y)
        self.pdf.ln(5)

    def text(self, title, subtitle):
        self.pdf.set_font("DejaVu-Bold", "", 9)
        self.pdf.write(2, title + " ")
        self.pdf.set_font("DejaVu", "", 7)
        self.pdf.write(2, subtitle + " ")

    def underline(self, text, list, idx):
        self.pdf.write(2, text + " ")
        flag = False
        for i in range(len(list)):
            if idx is not None and i == idx:
                x = self.pdf.get_x()
                y = self.pdf.get_y()
                flag = True
            if i == len(list) - 1:
                self.pdf.write(2, list[i].lower() + " ")
            else:
                self.pdf.write(2, list[i].lower() + ", ")
            if flag == True and idx is not None:
                self.pdf.line(x + 1, y + 2, self.pdf.get_x(), self.pdf.get_y() + 2)
                flag = False

    def input(self, text):
        self.pline()
        self.pdf.write(2, text)

    def static_pole(self, title, subtitle, text):
        if title != "":
            self.pdf.ln(1)
        self.pdf.set_font("DejaVu-Bold", "", 9)
        self.pdf.write(2, title)
        self.pdf.set_font("DejaVu", "", 7)
        self.pdf.write(2, subtitle + " ")
        self.pline()
        self.pdf.write(2, text)

    def multipole(self, list, text):
        for i in range(len(list)):
            self.pdf.write(2, list[i])
            x = self.pdf.get_x() + 2
            y = self.pdf.get_y()
            self.pdf.set_x(x + 5)
            self.pdf.write(2, text[i])
            self.pdf.set_x(self.pdf.get_x() + 5)
            if i == len(list) - 1:
                self.pdf.set_x(x)
                self.pline()
            else:
                self.pdf.line(x, y + 2, self.pdf.get_x(), y + 2)

    def gap(self, text, val):
        self.pdf.write(2, text)
        x = self.pdf.get_x() + 1
        y = self.pdf.get_y() + 2
        self.pdf.write(2, " " + val)
        self.pdf.set_x(self.pdf.get_x() + 1)
        self.pdf.line(x, y, self.pdf.get_x() + 1, y)

    def generate(self):
        self.pdf.output("Result.pdf", "F")
