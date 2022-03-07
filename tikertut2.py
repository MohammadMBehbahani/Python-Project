from tkinter import *
from tkinter import ttk


def set_entry(*args):
    entry_1_txt.set("Hello")


def chk_changed(*args):
    entry_1_txt.set(chk_1_txt.get())


def radio_change(*args):
    entry_1_txt.set(radio_1_val.get())


def combo_change(*args):
    entry_1_txt.set(combo_val.get())


root = Tk()
root.title("Widget Example")
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

label_1_txt = StringVar()
label_1 = ttk.Label(frame, textvariable='Data: ')
label_1.grid(column=1, row=1, sticky=(W, E))

label_1['textvariable'] = label_1_txt
label_1_txt.set('Data')

entry_1_txt = StringVar()
entry_1 = ttk.Entry(frame, width=7, textvariable=entry_1_txt)
entry_1.grid(column=2, row=1, sticky=(W, E))
entry_1_txt.set(label_1_txt.get())

button_1 = ttk.Button(frame, text="click", command=set_entry)
button_1.grid(column=1, row=2, sticky=(W, E))

button_1['state'] = 'disabled'
button_1['state'] = 'enable'

chk_1_txt = StringVar()
chk_1 = ttk.Checkbutton(frame, text='feeling', command=chk_changed,
                        variable=chk_1_txt,
                        onvalue="happy", offvalue="unhappy")
chk_1.grid(column=4, row=1, sticky=(W, E))


radio_1_val = StringVar()
red_but = ttk.Radiobutton(frame, text='Red', variable=radio_1_val,
                          value='red', command=radio_change)

blue_but = ttk.Radiobutton(frame, text='Blue', variable=radio_1_val,
                          value='Blue', command=radio_change)

green_but = ttk.Radiobutton(frame, text='Green', variable=radio_1_val,
                          value='Green', command=radio_change)

red_but.grid(column=2, row=2, sticky=(W, E))
blue_but.grid(column=3, row=2, sticky=(W, E))
green_but.grid(column=4, row=2, sticky=(W, E))

lbl_2 = ttk.Label(frame, text="Fav Color")
lbl_2.grid(column=1, row=2, sticky=(W, E))

combo_val = StringVar()
combo_1 = ttk.Combobox(frame, textvariable=combo_val)
labe_3 = ttk.Label(frame, text= "Size")
labe_3.grid(column=1, row=3, sticky=(W, E))
combo_1['values'] = ('Small', 'Medium', 'Large')
combo_1.grid(column=2, row=3, sticky=(W, E))

combo_1.bind('<<ComboboxSelected>>', combo_change)

root.mainloop()