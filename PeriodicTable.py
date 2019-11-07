"""
@author: NRG
"""

from tkinter import *
import Elements

class ElementFrame:

    def makeSquare(self, window, r, c, showInfoButton=True, showName=True, width=4, height=4, largeFont= "none 14", smallFont= "none 8"):
        # Coloring elements
        # TKinter color name chart: http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        color = "white"
        if self.element.number in [109,110,111,113,115,116,117,118]:color = "gray76"        # No defined section
        elif self.element.group == 1 and self.element.number != 1:  color = "orange"        # Alkali metals
        elif self.element.group == 2:                               color = "yellow2"       # Alkaline earth metals
        elif self.element.number in [13,31,49,50,81,82,83,84,114]:  color = "turquoise"     # Post-transition metals
        elif self.element.number in [5,14,32,33,51,52,85]:          color = "green3"        # Metalloids
        elif self.element.number in [1,6,7,8,9,15,16,17,34,35,53]:  color = "green2"        # Other nonmetals
        elif self.element.group == 18:                              color = "deep sky blue" # Noble gases
        elif self.element.group == "l":                             color = "lightpink1"    # Lanthanoids
        elif self.element.group == "a":                             color = "darksalmon"    # Actinoids. Dark Salmon sounds like a band name. Or a sith.
        else:                                                       color = "sandy brown"   # Assumed transition metals

        # Determine the symbol text color according to state at 300K. Red is gas, blue is liquid, gray is solid.
        state = self.element.stateAt(300)
        textColor = "red" if state == "gas" else "blue" if state == "liquid" else "black" if state == "solid" else "gray20"

        frame = Frame(window, height=2, width= width, bg=color, bd=3, highlightbackground="white", highlightthickness=1)
        frame.grid(row=r, column=c)

        # Frame for the top row, containing the numberLabel and infoButton. To avoid having a column 1 at below rows.
        topFrame = Frame(frame, height=1, width= width, bg=color, bd=0)
        topFrame.grid(row=0,column=0, sticky=E)
        
        numberLabel = Label(topFrame, text=self.element.number, font= smallFont, bg=color, height=1, width= width-1)
        numberLabel.grid(row=0, column=0, sticky=W)

        if showInfoButton:
            infoButton = Button(topFrame, text="i", font="none 6", command= lambda: self.elementInfo(), bg= color, height=1, width=1)
            infoButton.grid(row=0, column=2, sticky=E)
        
        symbolLabel = Label(frame, text=self.element.symbol, font= largeFont, bg=color, height=1, width= width)
        symbolLabel.grid(row=1, column=0)

        if showName:
            # Extend width beyond the frame to prevent the name of some of the longer named elements being cut off 
            nameLabel = Label(frame, text=self.element.name, font= smallFont, bg=color, height=1, width = width + 4)
            nameLabel.grid(row=2, column=0)

        

    def __init__(self, element, window):
        
        self.element = element

        # The variables for the row and column of the element frame. All those ternary operators are to place lanthanoids and actinoids below the table.
        r = element.period if not (element.group == "a" or element.group == "l") else (9 if element.group == "l" else 10)
        c = element.group  if not (element.group == "a" or element.group == "l") else ((element.number - 53) if element.group == "l" else element.number - 85) 
        
        self.makeSquare(window, r, c, showName=False)
        
    def elementInfo(self):
        
        infoWindow = Tk()
        infoWindow.title("Element info")


        topFrame = Frame(infoWindow, height=2, width= 10, bg="white", bd=3, highlightbackground="white", highlightthickness=1)
        topFrame.grid(row=0,column=0, sticky=W)
        
        self.makeSquare(topFrame, 0, 0, showInfoButton=False, showName=True, width=5, height=6, largeFont= "none 28", smallFont="none 14")

        topRightFrame = Frame(topFrame, height=2, width= 4, bg="white", bd=3, highlightbackground="white", highlightthickness=1)
        topRightFrame.grid(row=0,column=1)
        
        massLabel = Label(topRightFrame, text="Mass: " + str(self.element.mass) + "u", font="none 16")
        massLabel.grid(row=0, column=0, pady=2, sticky=W)

        boilingLabel = Label(topRightFrame, text="Boiling Point: " + str(self.element.boilingPoint) + "°K", font="none 16")
        boilingLabel.grid(row=1, column=0, pady=2, sticky=W)

        meltingLabel = Label(topRightFrame, text="Melting Point: " + str(self.element.meltingPoint) + "°K", font="none 16")
        meltingLabel.grid(row=2, column=0, pady=2, sticky=W)

        rcLabel = Label(infoWindow, text= "Group: " + str(self.element.group) + ", Period: " + str(self.element.period), font="none 16")
        rcLabel.grid(row=1, column=0, sticky=W)
        
        eConfigLabel = Label(infoWindow, text=self.element.eConfig, font = "none 14")
        eConfigLabel.grid(row=2, column=0, pady=2, sticky=W)

        isotopesFrame = Frame(infoWindow, height=3, width= 10)
        isotopesFrame.grid(row=3, column=0, sticky=W)

        i = 0
        for A in self.element.isotopes:
            isotope = self.element.isotopes[A]
            isotopeFrame = IsotopeFrame(isotopesFrame, isotope, i)
            i += 1
        

class IsotopeFrame:
    def __init__(self, window, isotope, c):
        self.isotope = isotope

        frame = Frame(window, height=4, width=4, bg="white", bd=3, highlightbackground="black", highlightthickness=1)
        frame.grid(row=0, column=c)

        topFrame = Frame(frame, height=2, width=3, bg="white")
        topFrame.grid(row=0, column=0)

        symbol = Elements.elements[isotope.protons].symbol    
        symbolLabel = Label(topFrame, text=symbol, font="none 28", width=2, height=2)
        symbolLabel.grid(row=0, column=1, sticky=W)

        # Frame for the numbers
        leftFrame = Frame(topFrame, height=2, width=1, bg="white")
        leftFrame.grid(row=0, column=0)
        aLabel = Label(leftFrame, text=isotope.nucleons, font="none 14", bg="white", height=1, width=1)
        zLabel = Label(leftFrame, text=isotope.protons , font="none 14", bg="white", height=1, width=1)
        aLabel.grid(row=0, column=0, sticky=E)
        zLabel.grid(row=1, column=0, sticky=E)

        massLabel = Label(frame, text=str(isotope.mass) + "u", font="none 10", bg="white", height=1, width=4)
        massLabel.grid(row=1, column=0, sticky=W+E)

        # TODO: Add decay modes and an add button


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
            l = Label(window, text=text, font= "none 12", bg="white", height=2, width= 4)
            l.grid(row=element.period, column=3)

    # Add an empty label at row 8, to space the detached element block from the rest of the table. Adjust its height to adjust the spacing.
    Label(window, text=" ", font= "none 16", bg="white", height=1, width= 0).grid(row=8, column=1)

    # Add label for periods
    for p in range(1,8):
        l = Label(window, text=p, font= "none 14", bg="white", height= 1, width=1)
        l.grid(row=p, column= 0)

    # Add label for groups
    for g in range(1,19):
        l = Label(window, text=g, font= "none 14", bg="white", height= 1, width=2)
        l.grid(row=0, column= g)

    window.mainloop()

PeriodicTable()







