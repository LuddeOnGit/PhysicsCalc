from tkinter import * 
from Python4Physics import *

def main():
    def u_to_kg():
        if len(uInput.get()) > 0:
            kgOutput["text"] = str(massConvU(float(uInput.get()))) + "kg"
    def kg_to_u():
        if len(kgInput.get()) > 0:
            uOutput["text"] = str(massConvKg(float(kgInput.get()))) + "u"
        
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

    """'
    kg to u
    """
    Label(window, text="Convert kg to u: ", font="none 12").grid(row=1, column=0, sticky=W)
    kgInput = Entry(window, width=8)
    kgInput.grid(row=1, column=1, sticky=W)
    uOutput = Label(window, text="0u", font="none 12")
    uOutput.grid(row=1, column=2, sticky=W)
    Button(window, text="SUBMIT", width=6, command=kg_to_u).grid(row=1, column=3, sticky=W)

    window.mainloop()


