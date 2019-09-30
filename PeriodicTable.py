#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: NRG
"""

from tkinter import *
import Elements

def PeriodicTable():
    window = Tk()
    window.title = "Periodic Table"

    def elementInfo(element):
        infoWindow = Tk()
        infotxt = str(element.info())
        infoLabel = Label(infoWindow, text=infotxt, font="none 16")
        infoLabel.grid(row=8, column=0, pady = 10, sticky=E)
    
    """
    Added to give the user an interactive periodic table, meant to click on an element and get pop-up with information
    """
        
    for element in Elements.elements:
        if type(element.group()) == int:
            #Lambda is used to prevent the function from running on startup so that you can add parameters to function call
            button = Button(window, text=element.symbol, font="none 16", command= lambda: elementInfo(element), height = 2, width = 3)
            button.grid(row=element.period(), column=element.group(), pady=2, sticky=W)
    
    window.mainloop()

PeriodicTable()
