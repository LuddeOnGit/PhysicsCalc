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
        if element.number in [109,110,111,113,115,116,117,118]:color = "gray76"        # No defined section
        elif element.group == 1 and element.number != 1:       color = "orange"        # Alkali metals
        elif element.group == 2:                               color = "yellow2"       # Alkaline earth metals
        elif element.number in [13,31,49,50,81,82,83,84,114]:  color = "turquoise"     # Post-transition metals
        elif element.number in [5,14,32,33,51,52,85]:          color = "green3"        # Metalloids
        elif element.number in [1,6,7,8,9,15,16,17,34,35,53]:  color = "green2"        # Other nonmetals
        elif element.group == 18:                              color = "deep sky blue" # Noble gases
        elif element.group == "l":                             color = "lightpink1"    # Lanthanoids
        elif element.group == "a":                             color = "darksalmon"    # Actinoids. Dark Salmon sounds like a band name. Or a sith.
        else:                                                  color = "sandy brown"   # Assumed transition metals

        # TODO: Find some way of giving info whereever you click on the frame. Maybe background hitbox?
        
        self.element = element

        # Determine the symbol text color according to state at 300K
        state = element.stateAt(300)
        textColor = "red" if state == "gas" else "blue" if state == "liquid" else "black" if state == "solid" else "gray20"


        # The variables for the row and column of the element frame. All those ternary operators are to place lanthanoids and actinoids below the table.
        r = element.period if not (element.group == "a" or element.group == "l") else (9 if element.group == "l" else 10)
        c = element.group  if not (element.group == "a" or element.group == "l") else ((element.number - 53) if element.group == "l" else element.number - 85) 
        
        self.frame = Frame(window, height=2, width= self.width, bg=color, bd=3, highlightbackground="white", highlightthickness=1)
        self.frame.grid(row=r, column=c)

        # Frame for the top row, containing the numberLabel and infoButton. To avoid having a column 1 at below rows.
        self.topFrame = Frame(self.frame, height=1, width= self.width, bg=color, bd=0)
        self.topFrame.grid(row=0,column=0, sticky=E)
        
        self.numberLabel = Label(self.topFrame, text=element.number, font= "none 10", bg=color, height=1, width= self.width-1)
        self.numberLabel.grid(row=0, column=0, sticky=W)

        self.infoButton = Button(self.topFrame, text="i", font="none 6", command= lambda: self.elementInfo(), bg= color, height=1, width=1)
        self.infoButton.grid(row=0, column=2, sticky=E)
        
        self.symbolLabel = Label(self.frame, text=element.symbol, font= "none 14", bg=color, height=1, width= self.width)
        self.symbolLabel.grid(row=1, column=0)
        self.symbolLabel.config(fg=textColor)

        # Extend width beyond the frame to prevent the name of some of the longer named elements being cut off 
        self.nameLabel = Label(self.frame, text=element.name, font= "none 8", bg=color, height=1, width = self.width + 4)
        self.nameLabel.grid(row=2, column=0)
        
    def elementInfo(self):
        infoWindow = Tk()
        infoWindow.title("Element info")
        infotxt = self.element.info()
        infoLabel = Label(infoWindow, text=infotxt, font="none 16")
        infoLabel.grid(row=8, column=0, pady = 10, sticky=E)

   
def PeriodicTable():
    window = Tk()
    window.title("Periodic Table")
    window.resizable(width=True, height=True)

    window.configure(background="white")

    """
    Added to give the user an interactive periodic table, meant to click on an element and get pop-up with information
    """
    elementFrames = []
        
    for element in Elements.elements:
        if element.number == 0: continue
       
        f = ElementFrame(element, window)
        elementFrames.append(f)
        
        if type(element.group) == str:
            text = "57-71" if element.number in range(57,71+1) else "89-103"
            l = Label(window, text=text, font= "none 16", bg="white", height=2, width= 5)
            l.grid(row=element.period, column=3)

    # Adds an empty label at row 8, to space the detached element block from the rest of the table. Adjust its height to adjust the spacing.
    Label(window, text=" ", font= "none 16", bg="white", height=1, width= 0).grid(row=8, column=1)

    window.mainloop()

PeriodicTable()







