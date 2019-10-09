"""
author: NRG
"""

from tkinter import * 
from Python4Physics import *
from Elements import *

class ins_and_outs:
    def __init__(self, unit, window):
        self.input = Entry(window, width=8)
        self.output = Label(window, text="0"+unit, font="none 12")
        

def main():
    class_instances = []
    def add_formula(row, unit, functionName, txt):
        class_instances.append(ins_and_outs(unit, window))
        
        class_instances[row].input.grid(row=row, column=1, sticky=W)
        class_instances[row].output.grid(row=row, column=2, sticky=W)

        Label(window, text=txt, font="none 12").grid(row=row, column=0, sticky=W)        
        Button(window, text="SUBMIT", width=6, command= lambda : functionName(row)).grid(row=row, column=3, sticky=W)

    def get_input(row):
        return class_instances[row].input.get()

    def set_output(row, output):
        class_instances[row].output["text"] = output
        
    def u_to_kg(row):
        if len(get_input(row)) > 0:
            output = str(massConvU(float(get_input(row)))) + "kg"
            set_output(row, output)
            
    def kg_to_u(row):
        if len(get_input(row)) > 0:
            output = str(massConvKg(float(get_input(row)))) + "u"
            set_output(row, output)
            
    def foEnergyToWl(row):
        if len(get_input(row)) > 0:
            output = str(wlPhoton(float(get_input(row)))) + "m"
            set_output(row, output)
            
    def massToEnergy(row):
        if len(get_input(row)) > 0:
            output = str(mass(float(get_input(row)))) + "J"
            set_output(row, output)
            
    def electronConfiguration(row):
        if len(get_input(row)) > 0:
            output = elements[int(get_input(row))].eConfig
            set_output(row, output)

    def enHyd(row):
        if len(get_input(row)) > 0:
            output = str(eHyd(int(get_input(row)))) + "J"
            set_output(row, output)

    def freqFromPeriod(row):
        if len(get_input(row)) > 0:
            output = str(freqOld(float(get_input(row)))) + "Hz"
            set_output(row, output)

    def fotonEnergy(row):
        if len(get_input(row)) > 0:
            output = str(ef(float(get_input(row)))) + "J"
            set_output(row, output)
    
    window = Tk()
    window.title("Physics Stuff")
    #window.configure(background = ""

    add_formula(0, "kg", u_to_kg, "Convert u to kg:")

    add_formula(1, "u", kg_to_u, "Convert kg to u:")

    add_formula(2, "m", foEnergyToWl, "Convert foton energy to wavelength:")

    add_formula(3, "J", massToEnergy, "Convert mass into energy using Einstein's formula:")   

    add_formula(4, " ", electronConfiguration, "Convert electron number to electron configuration:")

    add_formula(5, "J", enHyd, "Energy level for given shell:")

    add_formula(6, "Hz", freqFromPeriod, "Use period in s to calculate frequency")

    add_formula(7, "J", fotonEnergy, "Calculates foton energy from frequency")
    
    
    window.mainloop()


