#All frame definitions are stored here

import tkinter as tk
from tkinter import ttk


#Creates a new frame upon pressing "Get Started"
def start(start_frame, new_frame, root):
    root.title("Reactor select")
    start_frame.grid_forget()
    new_frame.grid(row = 0, column = 0, sticky = 'NSEW')
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)

#Adiabatic CSTR selection window
def adcstr(new_frame, adcstr_frame, root):
    root.title("Adiabatic CSTR")
    new_frame.grid_forget()
    adcstr_frame.grid(row = 0, column = 0, sticky = 'NSEW')

#Isothermal CSTR selection window
def isocstr(new_frame, isocstr_frame, root):
    root.title("Isothermal CSTR")
    new_frame.grid_forget()
    isocstr_frame.grid(row = 0, column = 0, sticky = 'NSEW')

#Adiabatic PFR selection window
def adpfr(new_frame, adpfr_frame, root):
    root.title("Adiabatic PFR")
    new_frame.grid_forget()
    adpfr_frame.grid(row = 0, column = 0, sticky = 'NSEW')

#Isothermal PFR selection window
def isopfr(new_frame, isopfr_frame, root):
    root.title("Isothermal PFR")
    new_frame.grid_forget()
    cstr_frame.grid(row = 0, column = 0, sticky = 'NSEW')

#Adiabatic PBR selection window
def adpbr(new_frame, adpbr_frame, root):
    root.title("Adiabatic PBR")
    new_frame.grid_forget()
    adpbr_frame.grid(row = 0, column = 0, sticky = 'NSEW')

#Isothermal PBR selection window
def isopbr(new_frame, isopbr_frame, root):
    root.title("Isothermal PBR")
    new_frame.grid_forget()
    isopbr_frame.grid(row = 0, column = 0, sticky = 'NSEW')

#Split new_frame into 6 frames in a grid
def bt_create(new_frame, row_num, col_num, button_name, description, command_name):
    bt = ttk.Frame(new_frame)
    bt.grid(row = row_num, column = col_num, sticky = 'NSEW')
    text_desc = tk.Text(bt, height = 5, width = 50)
    text_desc.tag_configure("center", justify='center')
    text_desc.insert("1.0", description)
    text_desc.tag_add("center", "1.0", "end")
    text_desc.pack(expand = True)
    button = ttk.Button(bt, text = button_name, command = command_name)
    button.pack(expand = True)
    new_frame.columnconfigure(col_num, weight = 1)
    new_frame.rowconfigure(row_num, weight = 1)

