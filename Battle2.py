import configparser
import os
import random
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import time

window = tkinter.Tk()

window.title("Minesweeper")

rows = 10
cols = 10
mines = 10

field = []
buttons = []

colors = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']

game_over = False


def createMenu():
    menubar = tkinter.Menu(window)
    menu_size = tkinter.Menu(window, tearoff=0)
    menu_size.add_command(label="small (10x10 with 10 mines)", command=lambda: setSize(10, 10, 10))
    menu_size.add_command(label="medium (20x20 with 40 mines)", command=lambda: setSize(20, 20, 40))
    menu_size.add_command(label="big (35x35 with 120 mines)", command=lambda: setSize(35, 35, 120))
    menu_size.add_separator()
    menubar.add_cascade(label="size", menu=menu_size)
    menubar.add_command(label="exit", command=lambda: window.destroy())
    menubar.add_command(label="AI Play", command=lambda: AI_PLAY())
    window.config(menu=menubar)


def AI_PLAY():
    while not game_over:
        x = random.randint(0, rows - 1)
        y = random.randint(0, cols - 1)
        clickOn(x, y, "Robot Lost")


def setSize(r, c, m):
    global rows, cols, mines
    rows = r
    cols = c
    mines = m
    saveConfig()
    restartGame()


def saveConfig():
    global rows, cols, mines
    config = configparser.ConfigParser()
    config.add_section("game")
    config.set("game", "rows", str(rows))
    config.set("game", "cols", str(cols))
    config.set("game", "mines", str(mines))
    config.add_section("sizes")

    with open("Minesweeper.ini", "w") as file:
        config.write(file)


def loadConfig():
    global rows, cols, mines
    config = configparser.ConfigParser()
    config.read("Minesweeper.ini")
    rows = config.getint("game", "rows")
    cols = config.getint("game", "cols")
    mines = config.getint("game", "mines")


def prepareGame():
    global rows, cols, mines, field
    field = []
    for x in range(0, rows):
        field.append([])
        for y in range(0, cols):
            #add button and init value for game
            field[x].append(0)
    #generate mines
    for _ in range(0, mines):
        x = random.randint(0, rows-1)
        y = random.randint(0, cols-1)
        #prevent spawning mine on top of each other
        while field[x][y] == -1:
            x = random.randint(0, rows-1)
            y = random.randint(0, cols-1)
        field[x][y] = -1
        if x != 0:
            if y != 0:
                if field[x-1][y-1] != -1:
                    field[x-1][y-1] = int(field[x-1][y-1]) + 1
            if field[x-1][y] != -1:
                field[x-1][y] = int(field[x-1][y]) + 1
            if y != cols-1:
                if field[x-1][y+1] != -1:
                    field[x-1][y+1] = int(field[x-1][y+1]) + 1
        if y != 0:
            if field[x][y-1] != -1:
                field[x][y-1] = int(field[x][y-1]) + 1
        if y != cols-1:
            if field[x][y+1] != -1:
                field[x][y+1] = int(field[x][y+1]) + 1
        if x != rows-1:
            if y != 0:
                if field[x+1][y-1] != -1:
                    field[x+1][y-1] = int(field[x+1][y-1]) + 1
            if field[x+1][y] != -1:
                field[x+1][y] = int(field[x+1][y]) + 1
            if y != cols-1:
                if field[x+1][y+1] != -1:
                    field[x+1][y+1] = int(field[x+1][y+1]) + 1


def prepareWindow():
    global rows, cols, buttons
    tkinter.Button(window, text="Restart", command=restartGame).grid(row=0, column=0, columnspan=cols, sticky=(W, E, S, N))
    buttons = []
    for x in range(0, rows):
        buttons.append([])
        for y in range(0, cols):
            b = tkinter.Button(window, text=" ", width=2, command=lambda x=x, y=y: clickOn(x, y, "You Lost"))
            b.grid(row=x+1, column=y, sticky=(W, E, S, N))
            buttons[x].append(b)


def restartGame():
    global game_over
    game_over = False
    for x in window.winfo_children():
        if type(x) != tkinter.Menu:
            x.destroy()
    prepareWindow()
    prepareGame()


def clickOn(x, y, message):
    global field, buttons, colors, game_over, rows, cols
    if game_over:
        return
    buttons[x][y]["text"] = str(field[x][y])
    if field[x][y] == -1:
        buttons[x][y]["text"] = "*"
        buttons[x][y].config(background='red', disabledforeground='black')
        game_over = True
        tkinter.messagebox.showinfo("Game Over", message)
        for _x in range(0, rows):
            for _y in range(cols):
                if field[_x][_y] == -1:
                    buttons[_x][_y]["text"] = "*"
    else:
        buttons[x][y].config(disabledforeground=colors[field[x][y]])
    if field[x][y] == 0:
        buttons[x][y]["text"] = " "
        autoClickOn(x, y)
    buttons[x][y]['state'] = 'disabled'
    buttons[x][y].config(relief=tkinter.SUNKEN)
    checkWin()


def autoClickOn(x, y):
    global field, buttons, colors, rows, cols
    if buttons[x][y]["state"] == "disabled":
        return
    if field[x][y] != 0:
        buttons[x][y]["text"] = str(field[x][y])
    else:
        buttons[x][y]["text"] = " "
    buttons[x][y].config(disabledforeground=colors[field[x][y]])
    buttons[x][y].config(relief=tkinter.SUNKEN)
    buttons[x][y]['state'] = 'disabled'
    if field[x][y] == 0:
        if x != 0 and y != 0:
            autoClickOn(x-1, y-1)
        if x != 0:
            autoClickOn(x-1, y)
        if x != 0 and y != cols-1:
            autoClickOn(x-1, y+1)
        if y != 0:
            autoClickOn(x, y-1)
        if y != cols-1:
            autoClickOn(x, y+1)
        if x != rows-1 and y != 0:
            autoClickOn(x+1, y-1)
        if x != rows-1:
            autoClickOn(x+1, y)
        if x != rows-1 and y != cols-1:
            autoClickOn(x+1, y+1)


def checkWin():
    global buttons, field, rows, cols
    win = True
    for x in range(0, rows):
        for y in range(0, cols):
            if field[x][y] != -1 and buttons[x][y]["state"] == "normal":
                win = False
    if win:
        tkinter.messagebox.showinfo("Gave Over", "You have won.")


if os.path.exists("Minesweeper.ini"):
    loadConfig()
else:
    saveConfig()


def main():
    createMenu()
    prepareWindow()
    prepareGame()
    window.mainloop()


main()


