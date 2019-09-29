#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:48:25 2019

@author: victorapeland
"""

from tkinter import *
import Elements


def PeriodicTable():
    window = Tk()
    window.title = "Periodic Table"
    
    """
    Added to give the user an interactive periodic table, ment to click on an element and get pop-up with information
    This isn't complete. Struggling to find a way to save element.number of every button, this is atleast a start
    """
        
    for element in Elements.elements:
        if type(element.group()) == int:
            #Lambda is used to prevent the function from running on startup
            button = Button(window, text=element.symbol, font="none 16", command= element.elementInfo)
            button.grid(row=element.period(), column=element.group(), pady=2, sticky=W)
            
    
    window.mainloop()

PeriodicTable()
