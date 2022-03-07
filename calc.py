from tkinter import *
from tkinter import ttk


class Calculator:
    calc_val = 0.0
    div_trigger = False
    add_trigger = False
    mult_trigger = False
    sub_trigger = False

    def button_click(self, value):
        if value == 'AC':
            self.div_trigger = False
            self.add_trigger = False
            self.mult_trigger = False
            self.sub_trigger = False
            self.num_entry.delete(0, "end")
            entry_val = 0
            self.num_entry.insert(0, entry_val)
        else:
            entry_val = self.num_entry.get()
            entry_val += value
            self.num_entry.delete(0, "end")
            self.num_entry.insert(0, entry_val)

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def math_but_click(self, value):
        if self.is_float(self.num_entry.get()):
            self.div_trigger = False
            self.add_trigger = False
            self.mult_trigger = False
            self.sub_trigger = False
            self.calc_val = float(self.entry_value.get())
            if value == "/":
                self.div_trigger = True

            elif value == "+":
                self.add_trigger = True

            elif value == "-":
                self.sub_trigger = True

            else:
                self.mult_trigger = True

            self.num_entry.delete(0, "end")

    def equal_but_click(self):
        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:
            if self.add_trigger:
                solution = self.calc_val + float(self.entry_value.get())

            elif self.sub_trigger:
                solution = self.calc_val - float(self.entry_value.get())

            elif self.mult_trigger:
                solution = self.calc_val * float(self.entry_value.get())

            else:
                solution = self.calc_val / float(self.entry_value.get())

            self.num_entry.delete(0, "end")
            self.num_entry.insert(0, solution)


    def __init__(self, root):
        self.entry_value = StringVar(root, value='')
        root.title("Calculator")
        root.geometry("480x220")
        root.resizable(width=False, height=False)
        # style = ttk.Style()
        # style.configure("TButton", font="Serif 15", padding=10)
        # style.configure("TEntry", font="Serif 18", padding=10)

        self.num_entry = ttk.Entry(root, textvariable=self.entry_value, width=50)
        self.num_entry.grid(row=0, column=4, sticky=(W, E))

        self.b7 = ttk.Button(root, text="7", command=lambda: self.button_click('7')).grid(column=1, row=1, sticky=(W, E))
        self.b8 = ttk.Button(root, text="8", command=lambda: self.button_click('8')).grid(column=2, row=1, sticky=(W, E))
        self.b9 = ttk.Button(root, text="9", command=lambda: self.button_click('9')).grid(column=3, row=1, sticky=(W, E))

        self.b9 = ttk.Button(root, text="/", command=lambda: self.math_but_click('/')).grid(column=4, row=1, sticky=(W, E))

        self.b4 = ttk.Button(root, text="4", command=lambda: self.button_click('4')).grid(column=1, row=2, sticky=(W, E))
        self.b5 = ttk.Button(root, text="5", command=lambda: self.button_click('5')).grid(column=2, row=2, sticky=(W, E))
        self.b6 = ttk.Button(root, text="6", command=lambda: self.button_click('6')).grid(column=3, row=2, sticky=(W, E))

        self.b9 = ttk.Button(root, text="*", command=lambda: self.math_but_click('*')).grid(column=4, row=2, sticky=(W, E))

        self.b1 = ttk.Button(root, text="1", command=lambda: self.button_click('1')).grid(column=1, row=3, sticky=(W, E))
        self.b2 = ttk.Button(root, text="2", command=lambda: self.button_click('2')).grid(column=2, row=3, sticky=(W, E))
        self.b3 = ttk.Button(root, text="3", command=lambda: self.button_click('3')).grid(column=3, row=3, sticky=(W, E))

        self.b9 = ttk.Button(root, text="+", command=lambda: self.math_but_click('+')).grid(column=4, row=3, sticky=(W, E))

        self.bac = ttk.Button(root, text="AC", command=lambda: self.button_click('AC')).grid(column=1, row=4, sticky=(W, E))
        self.b0 = ttk.Button(root, text="0", command=lambda: self.button_click('0')).grid(column=2, row=4, sticky=(W, E))
        self.beq = ttk.Button(root, text="=", command=lambda: self.equal_but_click()).grid(column=3, row=4, sticky=(W, E))

        self.bsub = ttk.Button(root, text="-", command=lambda: self.math_but_click('-')).grid(column=4, row=4, sticky=(W, E))


root = Tk()
calc = Calculator(root)
root.mainloop()