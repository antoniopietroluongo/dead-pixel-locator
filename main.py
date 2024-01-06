# -*- coding: utf-8 -*-
"""
@author: Antonio Pietroluongo

"""

import os
import tkinter
from tkinter import colorchooser, ttk

from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)


class DeadPixelLocator:
    def __init__(self):
        self.root = tkinter.Tk()
        self.bg = self.root.cget("background")
        self.root.title(os.getcwd())
        self.root.resizable(False, False)
        self.var = False
        self.label = tkinter.Label(self.root, text="Seleziona un colore per identificare un pixel bruciato.",
                                   justify="left")
        self.label.grid(row=0, column=0, sticky="W", pady=[5, 5])
        self.f = tkinter.Frame(master=self.root)
        self.f.grid(row=1, column=0, sticky="NSEW")
        self.red = ttk.Button(master=self.f, text="rosso", command=lambda: self.set_background("red"), width=5)
        self.red.pack(ipadx=5, ipady=5)
        self.lime = ttk.Button(master=self.f, text="lime", command=lambda: self.set_background("lime"), width=5)
        self.lime.pack(ipadx=5, ipady=5)
        self.blue = ttk.Button(master=self.f, text="blu", command=lambda: self.set_background("blue"), width=5)
        self.blue.pack(ipadx=5, ipady=5)
        self.white = ttk.Button(master=self.f, text="bianco", command=lambda: self.set_background("white"), width=5)
        self.white.pack(ipadx=5, ipady=5)
        self.black = ttk.Button(master=self.f, text="nero", command=lambda: self.set_background("black"), width=5)
        self.black.pack(ipadx=5, ipady=5)
        self.yellow = ttk.Button(master=self.f, text="giallo", command=lambda: self.set_background("yellow"), width=5)
        self.yellow.pack(ipadx=5, ipady=5)
        self.color_chooser = ttk.Button(master=self.f, text="...", command=self.choose_color, width=5)
        self.color_chooser.pack(ipadx=5, ipady=5)
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)
        self.root.bind("<Escape>", self.exit_fullscreen)
        self.root.bind("<Escape>", self.exit_fullscreen)
        self.root.bind("<Button-1>", self.exit_fullscreen)
        self.root.bind("<r>", lambda event: self.set_background("red"))
        self.root.bind("<l>", lambda event: self.set_background("lime"))
        self.root.bind("<b>", lambda event: self.set_background("blue"))
        self.root.bind("<w>", lambda event: self.set_background("white"))
        self.root.bind("<y>", lambda event: self.set_background("yellow"))
        self.root.bind("<R>", lambda event: self.set_background("red"))
        self.root.bind("<L>", lambda event: self.set_background("lime"))
        self.root.bind("<B>", lambda event: self.set_background("blue"))
        self.root.bind("<W>", lambda event: self.set_background("white"))
        self.root.bind("<Y>", lambda event: self.set_background("yellow"))
        self.root.bind("<c>", self.choose_color)
        self.root.bind("<C>", self.choose_color)

    def choose_color(self, event=None):
        color = colorchooser.askcolor(title="Scegli un colore")
        if color[1]:
            self.var = True
            self.label.grid_remove()
            self.f.grid_remove()
            self.root.configure(background=color[1])
            self.root.attributes('-fullscreen', True)

    def set_background(self, color):
        self.var = True
        self.label.grid_remove()
        self.f.grid_remove()
        self.root.configure(background=color)
        self.root.attributes('-fullscreen', True)

    def exit_fullscreen(self, event):
        if self.var:
            self.var = False
            self.root.attributes('-fullscreen', False)
            self.root.configure(background=self.bg)
            self.label.grid(row=0, column=0)
            self.f.grid(row=1, column=0)

    def show_window(self):
        self.root.mainloop()


if __name__ == '__main__':
    DeadPixelLocator().show_window()
