#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: NRG
"""

from tkinter import *
import Elements

class ElementFrame:
   
    # The width variable for the fram and its equally wide contents
    width = 4


    def __init__(self, element, window):

        # Coloring elements
        # TKinter color name chart: http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        color = "white"
        if element.group() == 1 and element.number != 1: color = "orange" # Alkali metals
        elif element.group() == 2: color = "yellow2"                      # Alkaline earth metals
        elif element.group() == 18: color = "deep sky blue"                # Noble gases

        # TODO: Find some way of giving info whereever you click on the frame. Maybe background hitbox?
        
        self.element = element

        self.frame = Frame(window, height = 2, width = self.width, bg=color, bd=2,highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.frame.grid(row=element.period(), column=element.group(), sticky=W)

        self.numberLabel = Label(self.frame, text=element.number, font= "none 12", bg=color, height=1, width= 2)
        self.numberLabel.grid(row=0, column=0, sticky=W)

        self.infoButton = Button(self.frame, text="i", font="none 12", command= lambda: self.elementInfo(), bg= color, height=1, width= 1)
        self.infoButton.grid(row=0, column=1,sticky=E)
        
        self.symbolLabel = Label(self.frame, text=element.symbol, font= "none 18", bg=color, height=1, width= self.width)
        self.symbolLabel.grid(row=1, column=0, sticky=W)

        # The name of some of the longer named elements is cut off because TKinter imagines a cell at r2c1. Possible fix in making a frame just for the top row (number and i)
        self.nameLabel = Label(self.frame, text=element.name, font= "none 8", bg=color, height=1, width = self.width)
        self.nameLabel.grid(row=2, column=0, sticky=W)
        
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
    elementFrames = []
        
    for element in Elements.elements:
        if type(element.group()) == int:
            f = ElementFrame(element, window)
            elementFrames.append(f)

    
    window.mainloop()

PeriodicTable()







