"""
author: NRG
"""

from tkinter import * 
from Python4Physics import *
from Elements import *

def main():
    inputs_and_outputs = {}
    def add_formula(ro, unit, functionName, txt, strFunctionName):
        input_key = f"{strFunctionName}_Input"
        output_key = f"{strFunctionName}_Output"
        
        input_entry = Entry(window, width=8)
        input_entry.grid(row=ro, column=1, sticky=W)
        
        output_label = Label(window, text="0"+unit, font="none 12")
        output_label.grid(row=ro, column=2, sticky=W)
        
        inputs_and_outputs[input_key] = input_entry
        inputs_and_outputs[output_key] = output_label
        
        Label(window, text=txt, font="none 12").grid(row=ro, column=0, sticky=W)        
        Button(window, text="SUBMIT", width=6, command=functionName).grid(row=ro, column=3, sticky=W)

    def get_input(strFunctionName):
        return inputs_and_outputs[f"{strFunctionName}_Input"].get()

    def set_output(strFunctionName, output):
        inputs_and_outputs[f"{strFunctionName}_Output"]["text"] = output
        
    def u_to_kg():
        if len(get_input("u_to_kg")) > 0:
            output = str(massConvU(float(get_input("u_to_kg")))) + "kg"
            set_output("u_to_kg", output)
            
    def kg_to_u():
        if len(get_input("kg_to_u")) > 0:
            output = str(massConvKg(float(get_input("kg_to_u")))) + "u"
            set_output("kg_to_u", output)
            
    def foEnergyToWl():
        if len(get_input("foEnergyToWl")) > 0:
            output = str(wlPhoton(float(get_input("foEnergyToWl")))) + "m"
            set_output("foEnergyToWl", output)
            
    def massToEnergy():
        if len(get_input("massToEnergy")) > 0:
            output = str(mass(float(get_input("massToEnergy")))) + "J"
            set_output("massToEnergy", output)
            
    def electronConfiguration():
        if len(get_input("electronConfiguration")) > 0:
            output = elements[int(get_input("electronConfiguration"))].eConfig()
            set_output("electronConfiguration", output)

    def enHyd():
        if len(get_input("enHyd")) > 0:
            output = str(eHyd(int(get_input("enHyd")))) + "J"
            set_output("enHyd", output)

    def freqFromPeriod():
        if len(get_input("freqFromPeriod")) > 0:
            output = str(freqOld(float(get_input("freqFromPeriod")))) + "Hz"
            set_output("freqFromPeriod", output)

    def fotonEnergy():
        if len(get_input("fotonEnergy")) > 0:
            output = str(ef(float(get_input("fotonEnergy")))) + "J"
            set_output("fotonEnergy", output)
    
    window = Tk()
    window.title("Physics Stuff")
    #window.configure(background = ""

    """
    u to kg
    """
    add_formula(0, "kg", u_to_kg, "Convert u to kg:", "u_to_kg")

    """
    kg to u
    """
    add_formula(1, "u", kg_to_u, "Convert kg to u:", "kg_to_u")

    """
    foton energy to wavelength
    """
    add_formula(2, "m", foEnergyToWl, "Convert foton energy to wavelength:", "foEnergyToWl")
    
    """
    E=mc^2
    """
    add_formula(3, "J", massToEnergy, "Convert mass into energy using Einstein's formula:", "massToEnergy")   
    """
    Electron configuration with orbital theory
    """
    add_formula(4, " ", electronConfiguration, "Convert electron number to electron configuration:", "electronConfiguration")
    """
    The energy level of a given electron shell (in Bohr's atomic model) for a hydrogen atom
    """
    add_formula(5, "J", enHyd, "energy level for given shell:", "enHyd")
    """
    Uses time to divide waves by time and get the frequency of a wave.
    """
    add_formula(6, "Hz", freqFromPeriod, "Use period in s to calculate frequency", "freqFromPeriod")
    """
    Calculates Energy of a given photon with frequency f.
    Takes Plancks-constant(h) and frequency(f)
    """
    add_formula(7, "J", fotonEnergy, "Calculates foton energy from frequency", "fotonEnergy")
    
    window.mainloop()


