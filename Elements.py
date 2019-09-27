#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:13:31 2019

@author: victorapeland
"""

class Element:
    
    # TODO: add mass and isotopes
    name = ""
    number = 0
    symbol = ""
    
    def __init__(self, number, symbol, name):
        self.number = number
        self.symbol = symbol
        self.name = name
        
    # Function to return a describing string
    def info(self):
        return f"{self.name} ({self.symbol}) has atomic number {self.number}"
    
    def period(self):
        if self.number <=   2: return 1
        if self.number <=  10: return 2
        if self.number <=  18: return 3
        if self.number <=  36: return 4
        if self.number <=  54: return 5
        if self.number <=  86: return 6
        if self.number <= 118: return 7
        
    

elements = [ 
    Element(number=   0, symbol= "Er", name= "Errorium"), # So the index is the same as the atomic number
    Element(number=   1, symbol= "H",  name= "Hydrogen"),
	Element(number=   2, symbol= "He", name= "Helium"),
	Element(number=   3, symbol= "Li", name= "Lithium"),
	Element(number=   4, symbol= "Be", name= "Beryllium"),
	Element(number=   5, symbol= "B",  name= "Boron"),
	Element(number=   6, symbol= "C",  name= "Carbon"),
	Element(number=   7, symbol= "N",  name= "Nitrogen"),
	Element(number=   8, symbol= "O",  name= "Oxygen"),
	Element(number=   9, symbol= "F",  name= "Fluorine"),
	Element(number=  10, symbol= "Ne", name= "Neon"),
	Element(number=  11, symbol= "Na", name= "Sodium"),
	Element(number=  12, symbol= "Mg", name= "Magnesium"),
	Element(number=  13, symbol= "Al", name= "Aluminium"),
	Element(number=  14, symbol= "Si", name= "Silicon"),
	Element(number=  15, symbol= "P",  name= "Phosphorus"),
	Element(number=  16, symbol= "S",  name= "Sulfur"),
	Element(number=  17, symbol= "Cl", name= "Chlorine"),
	Element(number=  18, symbol= "Ar", name= "Argon"),
	Element(number=  19, symbol= "K",  name= "Potassium"),
	Element(number=  20, symbol= "Ca", name= "Calcium"),
	Element(number=  21, symbol= "Sc", name= "Scandium"),
	Element(number=  22, symbol= "Ti", name= "Titanium"),
	Element(number=  23, symbol= "V",  name= "Vanadium"),
	Element(number=  24, symbol= "Cr", name= "Chromium"),
	Element(number=  25, symbol= "Mn", name= "Manganese"),
	Element(number=  26, symbol= "Fe", name= "Iron"),
	Element(number=  27, symbol= "Co", name= "Cobalt"),
	Element(number=  28, symbol= "Ni", name= "Nickel"),
	Element(number=  29, symbol= "Cu", name= "Copper"),
	Element(number=  30, symbol= "Zn", name= "Zinc"),
	Element(number=  31, symbol= "Ga", name= "Gallium"),
	Element(number=  32, symbol= "Ge", name= "Germanium"),
	Element(number=  33, symbol= "As", name= "Arsenic"),
	Element(number=  34, symbol= "Se", name= "Selenium"),
	Element(number=  35, symbol= "Br", name= "Bromine"),
	Element(number=  36, symbol= "Kr", name= "Krypton"),
	Element(number=  37, symbol= "Rb", name= "Rubidium"),
	Element(number=  38, symbol= "Sr", name= "Strontium"),
	Element(number=  39, symbol= "Y",  name= "Yttrium"),
	Element(number=  40, symbol= "Zr", name= "Zirconium"),
	Element(number=  41, symbol= "Nb", name= "Niobium"),
	Element(number=  42, symbol= "Mo", name= "Molybdenum"),
	Element(number=  43, symbol= "Tc", name= "Technetium"),
	Element(number=  44, symbol= "Ru", name= "Ruthenium"),
	Element(number=  45, symbol= "Rh", name= "Rhodium"),
	Element(number=  46, symbol= "Pd", name= "Palladium"),
	Element(number=  47, symbol= "Ag", name= "Silver"),
	Element(number=  48, symbol= "Cd", name= "Cadmium"),
	Element(number=  49, symbol= "In", name= "Indium"),
	Element(number=  50, symbol= "Sn", name= "Tin"),
	Element(number=  51, symbol= "Sb", name= "Antimony"),
	Element(number=  52, symbol= "Te", name= "Tellurium"),
	Element(number=  53, symbol= "I",  name= "Iodine"),
	Element(number=  54, symbol= "Xe", name= "Xenon"),
	Element(number=  55, symbol= "Cs", name= "Caesium"),
	Element(number=  56, symbol= "Ba", name= "Barium"),
	Element(number=  57, symbol= "La", name= "Lanthanum"),
	Element(number=  58, symbol= "Ce", name= "Cerium"),
	Element(number=  59, symbol= "Pr", name= "Praseodymium"),
	Element(number=  60, symbol= "Nd", name= "Neodymium"),
	Element(number=  61, symbol= "Pm", name= "Promethium"),
	Element(number=  62, symbol= "Sm", name= "Samarium"),
	Element(number=  63, symbol= "Eu", name= "Europium"),
	Element(number=  64, symbol= "Gd", name= "Gadolinium"),
	Element(number=  65, symbol= "Tb", name= "Terbium"),
	Element(number=  66, symbol= "Dy", name= "Dysprosium"),
	Element(number=  67, symbol= "Ho", name= "Holmium"),
	Element(number=  68, symbol= "Er", name= "Erbium"),
	Element(number=  69, symbol= "Tm", name= "Thulium"),
	Element(number=  70, symbol= "Yb", name= "Ytterbium"),
	Element(number=  71, symbol= "Lu", name= "Lutetium"),
	Element(number=  72, symbol= "Hf", name= "Hafnium"),
	Element(number=  73, symbol= "Ta", name= "Tantalum"),
	Element(number=  74, symbol= "W",  name= "Tungsten"),
	Element(number=  75, symbol= "Re", name= "Rhenium"),
	Element(number=  76, symbol= "Os", name= "Osmium"),
	Element(number=  77, symbol= "Ir", name= "Iridium"),
	Element(number=  78, symbol= "Pt", name= "Platinum"),
	Element(number=  79, symbol= "Au", name= "Gold"),
	Element(number=  80, symbol= "Hg", name= "Mercury"),
	Element(number=  81, symbol= "Tl", name= "Thallium"),
	Element(number=  82, symbol= "Pb", name= "Lead"),
	Element(number=  83, symbol= "Bi", name= "Bismuth"),
	Element(number=  84, symbol= "Po", name= "Polonium"),
	Element(number=  85, symbol= "At", name= "Astatine"),
	Element(number=  86, symbol= "Rn", name= "Radon"),
	Element(number=  87, symbol= "Fr", name= "Francium"),
	Element(number=  88, symbol= "Ra", name= "Radium"),
	Element(number=  89, symbol= "Ac", name= "Actinium"),
	Element(number=  90, symbol= "Th", name= "Thorium"),
	Element(number=  91, symbol= "Pa", name= "Protactinium"),
	Element(number=  92, symbol= "U",  name= "Uranium"),
	Element(number=  93, symbol= "Np", name= "Neptunium"),
	Element(number=  94, symbol= "Pu", name= "Plutonium"),
	Element(number=  95, symbol= "Am", name= "Americium"),
	Element(number=  96, symbol= "Cm", name= "Curium"),
	Element(number=  97, symbol= "Bk", name= "Berkelium"),
	Element(number=  98, symbol= "Cf", name= "Californium"),
	Element(number=  99, symbol= "Es", name= "Einsteinium"),
	Element(number= 100, symbol= "Fm", name= "Fermium"),
	Element(number= 101, symbol= "Md", name= "Mendelevium"),
	Element(number= 102, symbol= "No", name= "Nobelium"),
	Element(number= 103, symbol= "Lr", name= "Lawrencium"),
	Element(number= 104, symbol= "Rf", name= "Rutherfordium"),
	Element(number= 105, symbol= "Db", name= "Dubnium"),
	Element(number= 106, symbol= "Sg", name= "Seaborgium"),
	Element(number= 107, symbol= "Bh", name= "Bohrium"),
	Element(number= 108, symbol= "Hs", name= "Hassium"),
	Element(number= 109, symbol= "Mt", name= "Meitnerium"),
	Element(number= 110, symbol= "Ds", name= "Darmstadtium"),
	Element(number= 111, symbol= "Rg", name= "Roentgenium"),
	Element(number= 112, symbol= "Cn", name= "Copernicium"),
	Element(number= 113, symbol= "Nh", name= "Nihonium"),
	Element(number= 114, symbol= "Fl", name= "Flerovium"),
	Element(number= 115, symbol= "Mc", name= "Moscovium"),
	Element(number= 116, symbol= "Lv", name= "Livermorium"),
	Element(number= 117, symbol= "Ts", name= "Tennessine"),
	Element(number= 118, symbol= "Og", name= "Oganesson")
]