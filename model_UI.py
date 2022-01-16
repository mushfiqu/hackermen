import numpy as np
import tkinter as tk
from tkinter import ttk
import frame as fr
import sim_test as sim


#tkinter window settings
root = tk.Tk()
new_frame = ttk.Frame(root)
fr.bt_create(new_frame, 0, 0, "Adiabatic CSTR", "Simulates an Adiabatic CSTR reactor", lambda: fr.adcstr(new_frame, adcstr_frame, root))
fr.bt_create(new_frame, 1, 0, "Isothermal CSTR", "Simulates an Isothermal CSTR reactor", lambda: fr.isocstr(new_frame, isocstr_frame, root))
fr.bt_create(new_frame, 0, 1, "Adiabatic PFR", "Simulates an Adiabatic PFR reactor", lambda: fr.adpfr(new_frame, adcstr_frame, root))
fr.bt_create(new_frame, 1, 1, "Isothermal PFR", "Simulates an Isothermal PFR reactor", lambda: fr.isopfr(new_frame, isopfr_frame, root))
fr.bt_create(new_frame, 0, 2, "Adiabatic PBR", "Simulates an Adiabatic PBR reactor", lambda: fr.adpbr(new_frame, adpbr_frame, root))
fr.bt_create(new_frame, 1, 2, "Isothermal PBR", "Simulates an Isothermal PBR reactor", lambda: fr.isopbr(new_frame, isopbr_frame, root))
adcstr_frame = ttk.Frame(root)
isocstr_frame = ttk.Frame(root)
adpfr_frame = ttk.Frame(root)
isopfr_frame = ttk.Frame(root)
adpbr_frame = ttk.Frame(root)
isopbr_frame = ttk.Frame(root)

root.title("Solver")
root.geometry('800x480+50+50')
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
start_frame = ttk.Frame(root)
start_frame.grid(row = 0, column = 0, sticky = 'NSEW')

#Intro text
text_widget = tk.Text(start_frame, height = 5, width = 600)
text_widget.tag_configure("center", justify='center')
intro = "Plastic Pyrolis Solver\n"
howto = ("The following program will run simulations and model a plastic pyrolysis reactor.\n\
The user can pick between 4 different reactors to simulate the process: CSTR, PBR, PFR, Batch")

#Buttons 
get_started = ttk.Button(start_frame, text = 'Get Started', command = lambda: fr.start(start_frame, new_frame, root))
run_sim = ttk.Button(adcstr_frame, text = 'Run Test', command = lambda: sim.adCSTR())

#Buttons (new_frame)
#adcstr_select = ttk.Button(new_frame, text = 'Adiabatic CSTR', command = lambda: fr.adcstr(new_frame, adcstr_frame, root))
#isocstr_select = ttk.Button(new_frame, text = 'Isothermal CSTR', command = lambda: fr.isocstr(new_frame, isocstr_frame, root))
#adpfr_select = ttk.Button(new_frame, text = 'Adiabatic PFR', command = lambda: fr.adpfr(new_frame, adcstr_frame, root))
#isopfr_select = ttk.Button(new_frame, text = 'Isothermal PFR', command = lambda: fr.isopfr(new_frame, isopfr_frame, root))
#adpbr_select = ttk.Button(new_frame, text = 'Adiabatic PBR', command = lambda: fr.adpbr(new_frame, adpbr_frame, root))
#isopbr_select = ttk.Button(new_frame, text = 'Isothermal PBR', command = lambda: fr.isopbr(new_frame, isopbr_frame, root))

#Button Order
text_widget.pack()
text_widget.insert("1.0", intro)
text_widget.tag_add("center", "1.0", "end")
text_widget.insert("2.0", howto)
get_started.pack()
run_sim.pack()
root.mainloop()