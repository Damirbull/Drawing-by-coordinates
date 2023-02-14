from tkinter import Tk, Canvas, Frame, BOTH


class aboba(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Треугольник")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = aboba()
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()