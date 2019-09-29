from tkinter import * 
from Python4Physics import *
from Elements import *

def main():
    def u_to_kg():
        if len(uInput.get()) > 0:
            kgOutput["text"] = str(massConvU(float(uInput.get()))) + "kg"
    def kg_to_u():
        if len(kgInput.get()) > 0:
            uOutput["text"] = str(massConvKg(float(kgInput.get()))) + "u"
    def foEnergyToWl():
        if len(foEnInput.get()) > 0:
            wlOutput["text"] = str(wlPhoton(float(foEnInput.get()))) + "m"
    def massToEnergy():
        if len(massInput.get()) > 0:
            energyOutput["text"] = str(mass(float(massInput.get()))) + "J"
    def electronConfiguration():
        if len(elInput.get()) > 0:
            elOutput["text"] = str(Element.eConfig(elInput.get())) ##unsolved, gives error
        
    window = Tk()
    window.title("Physics Stuff")
    #window.configure(background = "")

    """
    u to kg
    """
    Label(window, text="Convert u to kg: ", font="none 12").grid(row=0, column=0, sticky=W)
    uInput = Entry(window, width=8)
    uInput.grid(row=0, column=1, sticky=W)
    kgOutput = Label(window, text="0kg", font="none 12")
    kgOutput.grid(row=0, column=2, sticky=W)
    Button(window, text="SUBMIT", width=6, command=u_to_kg).grid(row=0, column=3, sticky=W)

    """
    kg to u
    """
    Label(window, text="Convert kg to u: ", font="none 12").grid(row=1, column=0, sticky=W)
    kgInput = Entry(window, width=8)
    kgInput.grid(row=1, column=1, sticky=W)
    uOutput = Label(window, text="0u", font="none 12")
    uOutput.grid(row=1, column=2, sticky=W)
    Button(window, text="SUBMIT", width=6, command=kg_to_u).grid(row=1, column=3, sticky=W)

    """
    foton energy to wavelength
    """
    Label(window, text="Convert foton energy to wavelength: ", font="none 12").grid(row=2, column=0, sticky=W)
    foEnInput = Entry(window, width=8)
    foEnInput.grid(row=2, column=1, sticky=W)
    wlOutput = Label(window, text="0m", font="none 12")
    wlOutput.grid(row=2, column=2, sticky=W)
    Button(window, text="SUBMIT", width=6, command=foEnergyToWl).grid(row=2, column=3, sticky=W)
    
    """
    E=mc^2
    """
    Label(window, text="Converts mass into energy using Einsteins formula: ", font="none 12").grid(row=3, column=0, sticky=W)
    massInput = Entry(window, width=8)
    massInput.grid(row=3, column=1, sticky=W)
    energyOutput = Label(window, text="0J", font="none 12")
    energyOutput.grid(row=3, column=2, sticky=W)
    Button(window, text="SUBMIT", width=6, command=massToEnergy).grid(row=3, column=3, sticky=W)
    
    """
    Electron configuration with orbital theory
    """
    Label(window, text="Converts electron number to electron configuration: ", font="none 12").grid(row=4, column=0, sticky=W)
    elInput = Entry(window, width=8)
    elInput.grid(row=4, column=1, sticky=W)
    elOutput = Label(window, text="none", font="none 12")
    elOutput.grid(row=4, column=2, sticky=W)
    Button(window, text="SUBMIT", width=6, command=electronConfiguration).grid(row=4, column=3, sticky=W)    
    
    
    
    window.mainloop()
