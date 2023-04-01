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

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight = 1)

        for i in range(1,5):
            self.buttons_frame.rowconfigure(i, weight = 1)
            self.buttons_frame.columnconfigure(i, weight = 1)
        
        self.create_digit_buttons()

        
    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221, bg = LIGHT_GRAY)
        frame.pack(expand = True, fill = "both")
        return frame
    
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text = self.total_expression, 
                               anchor = tk.E, bg = LIGHT_GRAY, fg = LABEL_COLOR, padx = 24, font = SMALL_FONT_STYLE )
        total_label.pack(expand = True, fill = "both")

        label = tk.Label(self.display_frame, text = self.current_expression, 
                               anchor = tk.E, bg = LIGHT_GRAY, fg = LABEL_COLOR, padx = 24, font = LARGE_FONT_STYLE )
        label.pack(expand = True, fill = "both")

        return total_label, label 
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill = "both")
        return frame
    
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    
    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            buttom = tk.Button(self.buttons_frame, text = str(digit), bg = WHITE,
                                fg = LABEL_COLOR, font = DIGIT_FONT_STYLE, borderwidth = 0,
                                command = lambda x = digit: self.add_to_expression(x))
            buttom.grid(row = grid_value[0], column = grid_value[1], sticky = tk.NSEW)
    
    def update_label(self):
        self.label.config(text = self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    c = Calculator()
    c.run()