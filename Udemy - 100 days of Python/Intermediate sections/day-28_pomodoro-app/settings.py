from tkinter import *
import math

class Settings():
    def __init__(self):
        self.work_min = 25
        self.short_break_min = 5
        self.long_break_min = 20
        self.work_sessions_block = 4


    def dialog_get_user_input(self, parent):
        # create top level widget
        top = self.top = Toplevel(parent)
        top.attributes('-topmost',True)
        top.after_idle(top.attributes,'-topmost',False)
        top.focus_force()

        # work period input
        Label(top, text="Work minutes").grid(row=1, column=0)
        self.work_min_value = IntVar()
        self.work_min_value.set(self.work_min)
        self.work_min_input = Spinbox(top, textvariable=self.work_min_value, from_=1, to=100, width=5).grid(row=1, column=1, padx=5)
        
        # short break period
        Label(top, text="Short break minutes").grid(row=2, column=0)
        self.short_break_value = IntVar()
        self.short_break_value.set(self.short_break_min)
        self.short_break_input = Spinbox(top, textvariable=self.short_break_value, from_=1, to=100, width=5).grid(row=2, column=1, padx=5)

        Label(top, text="Long break minutes").grid(row=3, column=0)
        self.long_break_value = IntVar()
        self.long_break_value.set(self.long_break_min)
        self.long_break_input = Spinbox(top, textvariable=self.long_break_value, from_=1, to=100, width=5).grid(row=3, column=1, padx=5)

        Label(top, text="Work sessions per block").grid(row=4, column=0)
        self.work_sessions_block_value = IntVar()
        self.work_sessions_block_value.set(self.work_sessions_block)
        self.work_sessions_block_input = Spinbox(top, textvariable=self.work_sessions_block_value, from_=1, to=100, width=5).grid(row=4, column=1, padx=5)

        Button(top, text="OK", command=self.submit_settings).grid(row=5, column=1, pady=5)


    def submit_settings(self):
        self.work_min = int(self.work_min_value.get())
        self.short_break_min = int(self.short_break_value.get())
        self.long_break_min = int(self.long_break_value.get())
        self.work_sessions_block = int(self.work_sessions_block_value.get())
        self.top.destroy()