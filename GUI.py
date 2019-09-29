from tkinter import * 
from Python4Physics import *

def main():
    variable_names = {}
    def add_formula(ro, unit, functionName, txt, strFunctionName):
        variable_names[f"{strFunctionName}Input"] = Entry(window, width=8)
        variable_names[f"{strFunctionName}Output"] = Label(window, text="0"+unit, font="none 12")
        Label(window, text=txt, font="none 12").grid(row=ro, column=0, sticky=W)        
        variable_names[f"{strFunctionName}Input"].grid(row=ro, column=1, sticky=W)     
        variable_names[f"{strFunctionName}Output"].grid(row=ro, column=2, sticky=W)
        Button(window, text="SUBMIT", width=6, command=functionName).grid(row=ro, column=3, sticky=W)     
    def u_to_kg():
        if len(variable_names["u_to_kgInput"].get()) > 0:
            variable_names["u_to_kgOutput"]["text"] = str(massConvU(float(variable_names["u_to_kgInput"].get()))) + "kg"
    def kg_to_u():
        if len(variable_names["kg_to_uInput"].get()) > 0:
            variable_names["kg_to_uOutput"]["text"] = str(massConvKg(float(variable_names["kg_to_uInput"].get()))) + "u"
    def foEnergyToWl():
        if len(variable_names["foEnergyToWlInput"].get()) > 0:
            variable_names["foEnergyToWlOutput"]["text"] = str(wlPhoton(float(variable_names["foEnergyToWlInput"].get()))) + "m"
    def massToEnergy():
        if len(variable_names["massToEnergyInput"].get()) > 0:
            variable_names["massToEnergyOutput"]["text"] = str(mass(float(variable_names["massToEnergyInput"].get()))) + "J"
        
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
    add_formula(3, "J", massToEnergy, "Convert mass into energy using Einsteins formula:", "massToEnergy")
        
    window.mainloop()
