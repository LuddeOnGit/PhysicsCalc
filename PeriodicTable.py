#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: NRG
"""

from tkinter import *
import Elements

class ElementButton:
    element = Elements.elements[0]
    button = ""

    def __init__(self, element, window):
        self.element = element
        self.button = Button(window, text=element.symbol, font="none 16", command= lambda: self.elementInfo(), height = 2, width = 3)
        self.button.grid(row=element.period(), column=element.group(), pady=2, sticky=W)
        
    def elementInfo(self):
        infoWindow = Tk()
        infotxt = self.element.info()
        infoLabel = Label(infoWindow, text=infotxt, font="none 16")
        infoLabel.grid(row=8, column=0, pady = 10, sticky=E)


   
def PeriodicTable():
    window = Tk()
    window.title = "Periodic Table"

    """
    Added to give the user an interactive periodic table, meant to click on an element and get pop-up with information
    """
    elementButtons = []
        
    for element in Elements.elements:
        if type(element.group()) == int:
            button = ElementButton(element, window)
            elementButtons.append(button)

    
    window.mainloop()

PeriodicTable()







