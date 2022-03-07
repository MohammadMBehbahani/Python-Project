from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def quit_app():
    root.quit()


def show_about(*args):
    messagebox.showwarning("About", "Isn't this an awsome program?")


def change_font(event=None):
    print("Font change to", text_font.get())


root = Tk()
root.title("Menu Bar Example")
the_menu = Menu(root)

file_menu = Menu(the_menu, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)
the_menu.add_cascade(label="File", menu=file_menu)

view_menu = Menu(the_menu, tearoff=0)
line_numbers = IntVar()
line_numbers.set(1)
view_menu.add_checkbutton(label="Line Number", variable=line_numbers)
the_menu.add_cascade(label="View", menu=view_menu)

text_font = StringVar()
text_font.set("Times")
font_menu = Menu(the_menu, tearoff=0)
font_menu.add_radiobutton(label="Times",
                          variable=text_font,
                          command=change_font)
font_menu.add_radiobutton(label="Courier",
                          variable=text_font,
                          command=change_font)
font_menu.add_radiobutton(label="Arial",
                          variable=text_font,
                          command=change_font)
the_menu.add_cascade(label="Font", menu=font_menu)

help_menu = Menu(the_menu, tearoff=0)
help_menu.add_command(label="About",
                      accelerator="Command-A",
                      command=show_about)
the_menu.add_cascade(label="Help", menu=help_menu)

root.bind('<Command-A>', show_about)
root.bind('<Command-a>', show_about)

root.configure(menu=the_menu)

root.mainloop()