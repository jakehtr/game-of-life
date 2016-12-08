#!/usr/bin/env python3

from tkinter import *
from tkinter.ttk import *


class GUI:
    def __init__(self, title='Menu', columns=2, labels=None, buttons=None):
        self.master = Tk()
        self.master.wm_title(title)
        self.master.columnconfigure(1, weight=1)
        self.columns = columns - 1
        self.labels = []
        self.all_vars = []
        self.quit_button = ('Quit', self.master.quit)
        self.buttons = ([] if buttons is None else buttons) + [self.quit_button]

        if labels:
            for label_name, var, var_value in labels:
                var = var()
                var.set(var_value)
                self.labels.append((label_name, var))
                self.all_vars.append(var)

    def create(self):
        column_index = 0
        row_index = 0
        if self.labels:
            for label_name, var in self.labels:
                label = Label(self.master, text='{}'.format(label_name), width=25)
                entry = Entry(self.master, width=25, textvariable=var)

                label.grid(row=row_index, sticky=W, pady=5, padx=5)
                entry.grid(row=row_index, column=1, sticky=N + S + E + W, pady=5, padx=5)

                row_index += 1
        if self.buttons:
            for button_name, command in self.buttons:
                button = Button(self.master, text='{}'.format(button_name), command=command)
                button.grid(row=row_index, column=column_index, sticky=W, pady=5, padx=5)

                column_index += 1

                if column_index > self.columns:
                    column_index = 0
                    row_index += 1

            self.master.mainloop()

    def entries(self):
        return self.all_vars
