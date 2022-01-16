import numpy as np
import tkinter as tk
from tkinter import ttk
import frame as fr
import reactors as rc

#Display results
def display_adcstr():
    rc.adcstr(float(adcstr_CAo.get()),float(adcstr_Vr.get()),float(adcstr_vo.get()),float(adcstr_thetaB.get()),\
        float(adcstr_thetaI.get()),float(adcstr_To.get()),float(adcstr_T1.get()),float(adcstr_T2.get()))

def display_isocstr():
    rc.isocstr(float(isocstr_CAo.get()),float(isocstr_Vr.get()),float(isocstr_vo.get()),float(isocstr_thetaB.get()),\
        float(isocstr_thetaI.get()),float(isocstr_To.get()),float(isocstr_T1.get()),float(isocstr_T2.get()),\
        float(isocstr_Tc.get()),float(isocstr_U.get()),float(isocstr_SA.get()))
    
def display_adpfr():
    rc.adpfr(float(adpfr_CAo.get()),float(adpfr_Vr.get()),float(adpfr_vo.get()),float(adpfr_yAo.get()),\
        float(adpfr_thetaB.get()),float(adpfr_thetaI.get()),float(adpfr_To.get()))
    
def display_isopfr():
    rc.isopfr(float(isopfr_CAo.get()),float(isopfr_Vr.get()),float(isopfr_vo.get()),float(isopfr_yAo.get()),\
        float(isopfr_thetaB.get()),float(isopfr_thetaI.get()),float(isopfr_To.get()))
    
def display_adpbr():
    rc.adpbr(float(adpbr_CAo.get()),float(adpbr_Vr.get()),float(adpbr_vo.get()),float(adpbr_yAo.get()),\
        float(adpbr_thetaB.get()),float(adpbr_thetaI.get()),float(adpbr_To.get()),float(adpbr_alpha.get()),\
        float(adpbr_rho.get()),float(adpbr_BW.get()),float(adpbr_U.get()))
    
def display_isopbr():
    rc.isopbr(float(isopbr_CAo.get()),float(isopbr_Vr.get()),float(isopbr_vo.get()),float(isopbr_yAo.get()),\
        float(isopbr_thetaB.get()),float(isopbr_thetaI.get()),float(isopbr_To.get()),float(isopbr_Tc.get()),\
        float(isopbr_alpha.get()),float(isopbr_rho.get()),float(isopbr_U.get()),float(isopbr_mc.get()),float(isopbr_CpCool.get()),float(isopbr_SA.get()),float(isopbr_BW.get()))
    



#tkinter window settings
root = tk.Tk()
new_frame = ttk.Frame(root)
fr.bt_create(new_frame, 0, 0, "Adiabatic CSTR", "Simulates an Adiabatic CSTR reactor", lambda: fr.adcstr(new_frame, adcstr_frame, root))
fr.bt_create(new_frame, 1, 0, "Isothermal CSTR", "Simulates an Isothermal CSTR reactor", lambda: fr.isocstr(new_frame, isocstr_frame, root))
fr.bt_create(new_frame, 0, 1, "Adiabatic PFR", "Simulates an Adiabatic PFR reactor", lambda: fr.adpfr(new_frame, adpfr_frame, root))
fr.bt_create(new_frame, 1, 1, "Isothermal PFR", "Simulates an Isothermal PFR reactor", lambda: fr.isopfr(new_frame, isopfr_frame, root))
fr.bt_create(new_frame, 0, 2, "Adiabatic PBR", "Simulates an Adiabatic PBR reactor", lambda: fr.adpbr(new_frame, adpbr_frame, root))
fr.bt_create(new_frame, 1, 2, "Isothermal PBR", "Simulates an Isothermal PBR reactor", lambda: fr.isopbr(new_frame, isopbr_frame, root))


#Reactor frames
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
intro = "Plastic Pyrolysis Solver\n"
howto = ("The following program will run simulations and model a plastic pyrolysis reactor.\n\
The user can pick between 3 different reactor models to simulate the process: CSTR, PBR, PFR\n\
Each model can either be adiabatic (i.e. insulated) or isothermal (i.e. includes a heat exchanger)")

#Text entry (adCSTR)
tk.Label(adcstr_frame, text = "CAo").grid(row = 0)
tk.Label(adcstr_frame, text = "Vr").grid(row = 1)
tk.Label(adcstr_frame, text = "vo").grid(row = 2)
tk.Label(adcstr_frame, text = "thetaB").grid(row = 3)
tk.Label(adcstr_frame, text = "thetaI").grid(row = 4)
tk.Label(adcstr_frame, text = "To").grid(row = 5)
tk.Label(adcstr_frame, text = "T1").grid(row = 6)
tk.Label(adcstr_frame, text = "T2").grid(row = 7)

adcstr_CAo = tk.Entry(adcstr_frame)
adcstr_Vr = tk.Entry(adcstr_frame)
adcstr_vo = tk.Entry(adcstr_frame)
adcstr_thetaB = tk.Entry(adcstr_frame)
adcstr_thetaI = tk.Entry(adcstr_frame)
adcstr_To = tk.Entry(adcstr_frame)
adcstr_T1 = tk.Entry(adcstr_frame)
adcstr_T2 = tk.Entry(adcstr_frame)

adcstr_CAo.grid(row = 0, column = 1)
adcstr_Vr.grid(row = 1, column = 1)
adcstr_vo.grid(row = 2, column = 1)
adcstr_thetaB.grid(row = 3, column = 1)
adcstr_thetaI.grid(row = 4, column = 1)
adcstr_To.grid(row = 5, column = 1)
adcstr_T1.grid(row = 6, column = 1)
adcstr_T2.grid(row = 7, column = 1)

#Text entry (isoCSTR)
tk.Label(isocstr_frame, text = "CAo").grid(row = 0)
tk.Label(isocstr_frame, text = "Vr").grid(row = 1)
tk.Label(isocstr_frame, text = "vo").grid(row = 2)
tk.Label(isocstr_frame, text = "thetaB").grid(row = 3)
tk.Label(isocstr_frame, text = "thetaI").grid(row = 4)
tk.Label(isocstr_frame, text = "T1").grid(row = 5)
tk.Label(isocstr_frame, text = "T2").grid(row = 6)
tk.Label(isocstr_frame, text = "Tc").grid(row = 7)
tk.Label(isocstr_frame, text = "U").grid(row = 8)
tk.Label(isocstr_frame, text = "SA").grid(row = 9)
tk.Label(isocstr_frame, text = "To").grid(row = 10)

isocstr_CAo = tk.Entry(isocstr_frame)
isocstr_Vr = tk.Entry(isocstr_frame)
isocstr_vo = tk.Entry(isocstr_frame)
isocstr_thetaB = tk.Entry(isocstr_frame)
isocstr_thetaI = tk.Entry(isocstr_frame)
isocstr_T1 = tk.Entry(isocstr_frame)
isocstr_T2 = tk.Entry(isocstr_frame)
isocstr_Tc = tk.Entry(isocstr_frame)
isocstr_U = tk.Entry(isocstr_frame)
isocstr_SA = tk.Entry(isocstr_frame)
isocstr_To = tk.Entry(isocstr_frame)

isocstr_CAo.grid(row = 0, column = 1)
isocstr_Vr.grid(row = 1, column = 1)
isocstr_vo.grid(row = 2, column = 1)
isocstr_thetaB.grid(row = 3, column = 1)
isocstr_thetaI.grid(row = 4, column = 1)
isocstr_T1.grid(row = 5, column = 1)
isocstr_T2.grid(row = 6, column = 1)
isocstr_Tc.grid(row = 7, column = 1)
isocstr_U.grid(row = 8, column = 1)
isocstr_SA.grid(row = 9, column = 1)
isocstr_To.grid(row = 10, column = 1)

#Text entry (adpfr)
tk.Label(adpfr_frame, text = "CAo").grid(row = 0)
tk.Label(adpfr_frame, text = "Vr").grid(row = 1)
tk.Label(adpfr_frame, text = "vo").grid(row = 2)
tk.Label(adpfr_frame, text = "yAo").grid(row = 3)
tk.Label(adpfr_frame, text = "thetaB").grid(row = 4)
tk.Label(adpfr_frame, text = "thetaI").grid(row = 5)
tk.Label(adpfr_frame, text = "To").grid(row = 6)

adpfr_CAo = tk.Entry(adpfr_frame)
adpfr_Vr = tk.Entry(adpfr_frame)
adpfr_vo = tk.Entry(adpfr_frame)
adpfr_yAo = tk.Entry(adpfr_frame)
adpfr_thetaB = tk.Entry(adpfr_frame)
adpfr_thetaI = tk.Entry(adpfr_frame)
adpfr_To = tk.Entry(adpfr_frame)

adpfr_CAo.grid(row = 0, column = 1)
adpfr_Vr.grid(row = 1, column = 1)
adpfr_vo.grid(row = 2, column = 1)
adpfr_yAo.grid(row = 3, column = 1)
adpfr_thetaB.grid(row = 4, column = 1)
adpfr_thetaI.grid(row = 5, column = 1)
adpfr_To.grid(row = 6, column = 1)


#Text entry (isopfr)
tk.Label(isopfr_frame, text = "CAo").grid(row = 0)
tk.Label(isopfr_frame, text = "Vr").grid(row = 1)
tk.Label(isopfr_frame, text = "vo").grid(row = 2)
tk.Label(isopfr_frame, text = "yAo").grid(row = 3)
tk.Label(isopfr_frame, text = "thetaB").grid(row = 4)
tk.Label(isopfr_frame, text = "thetaI").grid(row = 5)
tk.Label(isopfr_frame, text = "To").grid(row = 6)

isopfr_CAo = tk.Entry(isopfr_frame)
isopfr_Vr = tk.Entry(isopfr_frame)
isopfr_vo = tk.Entry(isopfr_frame)
isopfr_yAo = tk.Entry(isopfr_frame)
isopfr_thetaB = tk.Entry(isopfr_frame)
isopfr_thetaI = tk.Entry(isopfr_frame)
isopfr_To = tk.Entry(isopfr_frame)

isopfr_CAo.grid(row = 0, column = 1)
isopfr_Vr.grid(row = 1, column = 1)
isopfr_vo.grid(row = 2, column = 1)
isopfr_yAo.grid(row = 3, column = 1)
isopfr_thetaB.grid(row = 4, column = 1)
isopfr_thetaI.grid(row = 5, column = 1)
isopfr_To.grid(row = 6, column = 1)

#Text entry (adpbr)
tk.Label(adpbr_frame, text = "CAo").grid(row = 0)
tk.Label(adpbr_frame, text = "Vr").grid(row = 1)
tk.Label(adpbr_frame, text = "vo").grid(row = 2)
tk.Label(adpbr_frame, text = "yAo").grid(row = 3)
tk.Label(adpbr_frame, text = "thetaB").grid(row = 4)
tk.Label(adpbr_frame, text = "thetaI").grid(row = 5)
tk.Label(adpbr_frame, text = "To").grid(row = 6)
tk.Label(adpbr_frame, text = "alpha").grid(row = 7)
tk.Label(adpbr_frame, text = "rho").grid(row = 8)
tk.Label(adpbr_frame, text = "BW").grid(row = 9)
tk.Label(adpbr_frame, text = "U").grid(row = 10)

adpbr_CAo = tk.Entry(adpbr_frame)
adpbr_Vr = tk.Entry(adpbr_frame)
adpbr_vo = tk.Entry(adpbr_frame)
adpbr_yAo = tk.Entry(adpbr_frame)
adpbr_thetaB = tk.Entry(adpbr_frame)
adpbr_thetaI = tk.Entry(adpbr_frame)
adpbr_To = tk.Entry(adpbr_frame)
adpbr_alpha = tk.Entry(adpbr_frame)
adpbr_rho = tk.Entry(adpbr_frame)
adpbr_BW = tk.Entry(adpbr_frame)
adpbr_U = tk.Entry(adpbr_frame)


adpbr_CAo.grid(row = 0, column = 1)
adpbr_Vr.grid(row = 1, column = 1)
adpbr_vo.grid(row = 2, column = 1)
adpbr_yAo.grid(row = 3, column = 1)
adpbr_thetaB.grid(row = 4, column = 1)
adpbr_thetaI.grid(row = 5, column = 1)
adpbr_To.grid(row = 6, column = 1)
adpbr_alpha.grid(row = 7, column = 1)
adpbr_rho.grid(row = 8, column = 1)
adpbr_BW.grid(row = 9, column = 1)
adpbr_U.grid(row = 10, column = 1)

#Text entry (isopbr)
tk.Label(isopbr_frame, text = "CAo").grid(row = 0)
tk.Label(isopbr_frame, text = "Vr").grid(row = 1)
tk.Label(isopbr_frame, text = "vo").grid(row = 2)
tk.Label(isopbr_frame, text = "yAo").grid(row = 3)
tk.Label(isopbr_frame, text = "thetaB").grid(row = 4)
tk.Label(isopbr_frame, text = "thetaI").grid(row = 5)
tk.Label(isopbr_frame, text = "To").grid(row = 6)
tk.Label(isopbr_frame, text = "Tc").grid(row = 7)
tk.Label(isopbr_frame, text = "alpha").grid(row = 8)
tk.Label(isopbr_frame, text = "rho").grid(row = 9)
tk.Label(isopbr_frame, text = "U").grid(row = 10)
tk.Label(isopbr_frame, text = "mc").grid(row = 11)
tk.Label(isopbr_frame, text = "CpCool").grid(row = 12)
tk.Label(isopbr_frame, text = "SA").grid(row = 13)
tk.Label(isopbr_frame, text = "BW").grid(row = 14)

isopbr_CAo = tk.Entry(isopbr_frame)
isopbr_Vr = tk.Entry(isopbr_frame)
isopbr_vo = tk.Entry(isopbr_frame)
isopbr_yAo = tk.Entry(isopbr_frame)
isopbr_thetaB = tk.Entry(isopbr_frame)
isopbr_thetaI = tk.Entry(isopbr_frame)
isopbr_To = tk.Entry(isopbr_frame)
isopbr_Tc = tk.Entry(isopbr_frame)
isopbr_alpha = tk.Entry(isopbr_frame)
isopbr_rho = tk.Entry(isopbr_frame)
isopbr_U = tk.Entry(isopbr_frame)
isopbr_mc = tk.Entry(isopbr_frame)
isopbr_CpCool = tk.Entry(isopbr_frame)
isopbr_SA = tk.Entry(isopbr_frame)
isopbr_BW = tk.Entry(isopbr_frame)


isopbr_CAo.grid(row = 0, column = 1)
isopbr_Vr.grid(row = 1, column = 1)
isopbr_vo.grid(row = 2, column = 1)
isopbr_yAo.grid(row = 3, column = 1)
isopbr_thetaB.grid(row = 4, column = 1)
isopbr_thetaI.grid(row = 5, column = 1)
isopbr_To.grid(row = 6, column = 1)
isopbr_Tc.grid(row = 7, column = 1)
isopbr_alpha.grid(row = 8, column = 1)
isopbr_rho.grid(row = 9, column = 1)
isopbr_U.grid(row = 10, column = 1)
isopbr_mc.grid(row = 11, column = 1)
isopbr_CpCool.grid(row = 12, column = 1)
isopbr_SA.grid(row = 13, column = 1)
isopbr_BW.grid(row = 14, column = 1)


#Buttons 
get_started = ttk.Button(start_frame, text = 'Get Started', command = lambda: fr.start(start_frame, new_frame, root))
adcstr_results = ttk.Button(adcstr_frame, text = 'Display Results', command = lambda: display_adcstr()).grid()
isocstr_results = ttk.Button(isocstr_frame, text = 'Display Results', command = lambda: display_isocstr()).grid()
adpfr_results = ttk.Button(adpfr_frame, text = 'Display Results', command = lambda: display_adpfr()).grid()
isopfr_results = ttk.Button(isopfr_frame, text = 'Display Results', command = lambda: display_isopfr()).grid()
adpbr_results = ttk.Button(adpbr_frame, text = 'Display Results', command = lambda: display_adpbr()).grid()
isopbr_results = ttk.Button(isopbr_frame, text = 'Display Results', command = lambda: display_isopbr()).grid()


#Button Order
text_widget.pack()
text_widget.insert("1.0", intro)
text_widget.tag_add("center", "1.0", "end")
text_widget.insert("2.0", howto)
get_started.pack()
root.mainloop()