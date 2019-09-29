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
        
    def u_to_kg():
        if len(inputs_and_outputs["u_to_kg_Input"].get()) > 0:
            inputs_and_outputs["u_to_kg_Output"]["text"] = str(massConvU(float(inputs_and_outputs["u_to_kg_Input"].get()))) + "kg"
            
    def kg_to_u():
        if len(inputs_and_outputs["kg_to_u_Input"].get()) > 0:
            inputs_and_outputs["kg_to_u_Output"]["text"] = str(massConvKg(float(inputs_and_outputs["kg_to_u_Input"].get()))) + "u"
            
    def foEnergyToWl():
        if len(inputs_and_outputs["foEnergyToWl_Input"].get()) > 0:
            inputs_and_outputs["foEnergyToWl_Output"]["text"] = str(wlPhoton(float(inputs_and_outputs["foEnergyToWl_Input"].get()))) + "m"
            
    def massToEnergy():
        if len(inputs_and_outputs["massToEnergy_Input"].get()) > 0:
            inputs_and_outputs["massToEnergy_Output"]["text"] = str(mass(float(inputs_and_outputs["massToEnergy_Input"].get()))) + "J"
            
    def electronConfiguration():
        if len(inputs_and_outputs["electronConfiguration_Input"].get()) > 0:
            inputs_and_outputs["electronConfiguration_Output"]["text"] = elements[int(inputs_and_outputs["electronConfiguration_Input"].get())].eConfig() 
        
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
    
    window.mainloop()
