import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F5F5F5"
LIGHT_BLUE = "#CCEDFF"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.title("Calculator")
        self.window.resizable(0,0)


    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    c = Calculator()
    c.run()