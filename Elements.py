#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:13:31 2019

@author: victorapeland
"""

class Element:
    
    # TODO: add isotopes
    name = ""
    number = 0
    symbol = ""
    boilingPoint = ""
    meltingPoint = ""
    
    def __init__(self, number, symbol, name, boilingPoint, meltingPoint, mass):
        self.number = number
        self.symbol = symbol
        self.name = name
        self.boilingPoint = boilingPoint
        self.meltingPoint = meltingPoint
        self.mass = mass
        
    # Function to return a describing string
    def info(self):
        return f"{self.name} ({self.symbol}) has atomic number {self.number}, {self.mass}u atomic mass, {self.meltingPoint}K melting point and {self.boilingPoint}K boiling point."
    
    def period(self):
        if self.number <=   2: return 1
        if self.number <=  10: return 2
        if self.number <=  18: return 3
        if self.number <=  36: return 4
        if self.number <=  54: return 5
        if self.number <=  86: return 6
        if self.number <= 118: return 7
        
elements = [
    Element(number=  0, symbol= "Er", name= "Errorium", boilingPoint= "Error", meltingPoint= "Error", mass= "Error"), # So the index is the same as the atomic number
    Element(number=  1, symbol= "H", name= "Hydrogen", boilingPoint= 20.28, meltingPoint= 13.81, mass= 1.00794),
    Element(number=  2, symbol= "He", name= "Helium", boilingPoint= 4.216, meltingPoint= 0.95, mass= 4.0026),
    Element(number=  3, symbol= "Li", name= "Lithium", boilingPoint= 1615, meltingPoint= 453.7, mass= 6.941),
    Element(number=  4, symbol= "Be", name= "Beryllium", boilingPoint= 3243, meltingPoint= 1560, mass= 9.01218),
    Element(number=  5, symbol= "B", name= "Boron", boilingPoint= 4275, meltingPoint= 2365, mass= 10.811),
    Element(number=  6, symbol= "C", name= "Carbon", boilingPoint= 5100, meltingPoint= 3825, mass= 12.011),
    Element(number=  7, symbol= "N", name= "Nitrogen", boilingPoint= 77.344, meltingPoint= 63.15, mass= 14.0067),
    Element(number=  8, symbol= "O", name= "Oxygen", boilingPoint= 90.188, meltingPoint= 54.8, mass= 15.9994),
    Element(number=  9, symbol= "F", name= "Fluorine", boilingPoint= 85, meltingPoint= 53.55, mass= 18.9984),
    Element(number= 10, symbol= "Ne", name= "Neon", boilingPoint= 27.1, meltingPoint= 24.55, mass= 20.1797),
    Element(number= 11, symbol= "Na", name= "Sodium", boilingPoint= 1156, meltingPoint= 371, mass= 22.98977),
    Element(number= 12, symbol= "Mg", name= "Magnesium", boilingPoint= 1380, meltingPoint= 922, mass= 24.305),
    Element(number= 13, symbol= "Al", name= "Aluminium", boilingPoint= 2740, meltingPoint= 933.5, mass= 26.98154),
    Element(number= 14, symbol= "Si", name= "Silicon", boilingPoint= 2630, meltingPoint= 1683, mass= 28.0855),
    Element(number= 15, symbol= "P", name= "Phosphorus", boilingPoint= 553, meltingPoint= 317.3, mass= 30.97376),
    Element(number= 16, symbol= "S", name= "Sulfur", boilingPoint= 717.82, meltingPoint= 392.2, mass= 32.066),
    Element(number= 17, symbol= "Cl", name= "Chlorine", boilingPoint= 239.18, meltingPoint= 172.17, mass= 35.4527),
    Element(number= 18, symbol= "Ar", name= "Argon", boilingPoint= 87.45, meltingPoint= 83.95, mass= 39.948),
    Element(number= 19, symbol= "K", name= "Potassium", boilingPoint= 1033, meltingPoint= 336.8, mass= 39.0983),
    Element(number= 20, symbol= "Ca", name= "Calcium", boilingPoint= 1757, meltingPoint= 1112, mass= 40.078),
    Element(number= 21, symbol= "Sc", name= "Scandium", boilingPoint= 3109, meltingPoint= 1814, mass= 44.9559),
    Element(number= 22, symbol= "Ti", name= "Titanium", boilingPoint= 3560, meltingPoint= 1945, mass= 47.88),
    Element(number= 23, symbol= "V", name= "Vanadium", boilingPoint= 3650, meltingPoint= 2163, mass= 50.9415),
    Element(number= 24, symbol= "Cr", name= "Chromium", boilingPoint= 2945, meltingPoint= 2130, mass= 51.996),
    Element(number= 25, symbol= "Mn", name= "Manganese", boilingPoint= 2335, meltingPoint= 1518, mass= 54.938),
    Element(number= 26, symbol= "Fe", name= "Iron", boilingPoint= 3023, meltingPoint= 1808, mass= 55.847),
    Element(number= 27, symbol= "Co", name= "Cobalt", boilingPoint= 3143, meltingPoint= 1768, mass= 58.9332),
    Element(number= 28, symbol= "Ni", name= "Nickel", boilingPoint= 3005, meltingPoint= 1726, mass= 58.6934),
    Element(number= 29, symbol= "Cu", name= "Copper", boilingPoint= 2840, meltingPoint= 1356.6, mass= 63.546),
    Element(number= 30, symbol= "Zn", name= "Zinc", boilingPoint= 1180, meltingPoint= 692.73, mass= 65.39),
    Element(number= 31, symbol= "Ga", name= "Gallium", boilingPoint= 2478, meltingPoint= 302.92, mass= 69.723),
    Element(number= 32, symbol= "Ge", name= "Germanium", boilingPoint= 3107, meltingPoint= 1211.5, mass= 72.61),
    Element(number= 33, symbol= "As", name= "Arsenic", boilingPoint= 876, meltingPoint= 1090, mass= 74.9216),
    Element(number= 34, symbol= "Se", name= "Selenium", boilingPoint= 958, meltingPoint= 494, mass= 78.96),
    Element(number= 35, symbol= "Br", name= "Bromine", boilingPoint= 331.85, meltingPoint= 265.95, mass= 79.904),
    Element(number= 36, symbol= "Kr", name= "Krypton", boilingPoint= 120.85, meltingPoint= 116, mass= 83.8),
    Element(number= 37, symbol= "Rb", name= "Rubidium", boilingPoint= 961, meltingPoint= 312.63, mass= 85.4678),
    Element(number= 38, symbol= "Sr", name= "Strontium", boilingPoint= 1655, meltingPoint= 1042, mass= 87.62),
    Element(number= 39, symbol= "Y", name= "Yttrium", boilingPoint= 3611, meltingPoint= 1795, mass= 88.9059),
    Element(number= 40, symbol= "Zr", name= "Zirconium", boilingPoint= 4682, meltingPoint= 2128, mass= 91.224),
    Element(number= 41, symbol= "Nb", name= "Niobium", boilingPoint= 5015, meltingPoint= 2742, mass= 92.9064),
    Element(number= 42, symbol= "Mo", name= "Molybdenum", boilingPoint= 4912, meltingPoint= 2896, mass= 95.94),
    Element(number= 43, symbol= "Tc", name= "Technetium", boilingPoint= 4538, meltingPoint= 2477, mass= 98),
    Element(number= 44, symbol= "Ru", name= "Ruthenium", boilingPoint= 4425, meltingPoint= 2610, mass= 101.07),
    Element(number= 45, symbol= "Rh", name= "Rhodium", boilingPoint= 3970, meltingPoint= 2236, mass= 102.9055),
    Element(number= 46, symbol= "Pd", name= "Palladium", boilingPoint= 3240, meltingPoint= 1825, mass= 106.42),
    Element(number= 47, symbol= "Ag", name= "Silver", boilingPoint= 2436, meltingPoint= 1235.08, mass= 107.868),
    Element(number= 48, symbol= "Cd", name= "Cadmium", boilingPoint= 1040, meltingPoint= 594.26, mass= 112.41),
    Element(number= 49, symbol= "In", name= "Indium", boilingPoint= 2350, meltingPoint= 429.78, mass= 114.82),
    Element(number= 50, symbol= "Sn", name= "Tin", boilingPoint= 2876, meltingPoint= 505.12, mass= 114.82),
    Element(number= 51, symbol= "Sb", name= "Antimony", boilingPoint= 1860, meltingPoint= 903.91, mass= 118.71),
    Element(number= 52, symbol= "Te", name= "Tellurium", boilingPoint= 1261, meltingPoint= 722.72, mass= 121.757),
    Element(number= 53, symbol= "I", name= "Iodine", boilingPoint= 457.5, meltingPoint= 386.7, mass= 127.6),
    Element(number= 54, symbol= "Xe", name= "Xenon", boilingPoint= 165.1, meltingPoint= 161.39, mass= 126.9045),
    Element(number= 55, symbol= "Cs", name= "Caesium", boilingPoint= 944, meltingPoint= 301.54, mass= 131.29),
    Element(number= 56, symbol= "Ba", name= "Barium", boilingPoint= 2078, meltingPoint= 1002, mass= 132.9054),
    Element(number= 57, symbol= "La", name= "Lanthanum", boilingPoint= 3737, meltingPoint= 1191, mass= 137.33),
    Element(number= 58, symbol= "Ce", name= "Cerium", boilingPoint= 3715, meltingPoint= 1071, mass= 138.9055),
    Element(number= 59, symbol= "Pr", name= "Praseodymium", boilingPoint= 3785, meltingPoint= 1204, mass= 140.12),
    Element(number= 60, symbol= "Nd", name= "Neodymium", boilingPoint= 3347, meltingPoint= 1294, mass= 140.9077),
    Element(number= 61, symbol= "Pm", name= "Promethium", boilingPoint= 3273, meltingPoint= 1315, mass= 144.24),
    Element(number= 62, symbol= "Sm", name= "Samarium", boilingPoint= 2067, meltingPoint= 1347, mass= 145),
    Element(number= 63, symbol= "Eu", name= "Europium", boilingPoint= 1800, meltingPoint= 1095, mass= 150.36),
    Element(number= 64, symbol= "Gd", name= "Gadolinium", boilingPoint= 3545, meltingPoint= 1585, mass= 151.965),
    Element(number= 65, symbol= "Tb", name= "Terbium", boilingPoint= 3500, meltingPoint= 1629, mass= 157.25),
    Element(number= 66, symbol= "Dy", name= "Dysprosium", boilingPoint= 2840, meltingPoint= 1685, mass= 158.9253),
    Element(number= 67, symbol= "Ho", name= "Holmium", boilingPoint= 2968, meltingPoint= 1747, mass= 162.5),
    Element(number= 68, symbol= "Er", name= "Erbium", boilingPoint= 3140, meltingPoint= 1802, mass= 164.9303),
    Element(number= 69, symbol= "Tm", name= "Thulium", boilingPoint= 2223, meltingPoint= 1818, mass= 167.26),
    Element(number= 70, symbol= "Yb", name= "Ytterbium", boilingPoint= 1469, meltingPoint= 1092, mass= 168.9342),
    Element(number= 71, symbol= "Lu", name= "Lutetium", boilingPoint= 3668, meltingPoint= 1936, mass= 173.04),
    Element(number= 72, symbol= "Hf", name= "Hafnium", boilingPoint= 4875, meltingPoint= 2504, mass= 174.967),
    Element(number= 73, symbol= "Ta", name= "Tantalum", boilingPoint= 5730, meltingPoint= 3293, mass= 178.49),
    Element(number= 74, symbol= "W", name= "Tungsten", boilingPoint= 5825, meltingPoint= 3695, mass= 180.9479),
    Element(number= 75, symbol= "Re", name= "Rhenium", boilingPoint= 5870, meltingPoint= 3455, mass= 183.85),
    Element(number= 76, symbol= "Os", name= "Osmium", boilingPoint= 5300, meltingPoint= 3300, mass= 186.207),
    Element(number= 77, symbol= "Ir", name= "Iridium", boilingPoint= 4700, meltingPoint= 2720, mass= 190.2),
    Element(number= 78, symbol= "Pt", name= "Platinum", boilingPoint= 4100, meltingPoint= 2042.1, mass= 192.22),
    Element(number= 79, symbol= "Au", name= "Gold", boilingPoint= 3130, meltingPoint= 1337.58, mass= 195.08),
    Element(number= 80, symbol= "Hg", name= "Mercury", boilingPoint= 629.88, meltingPoint= 234.31, mass= 196.9665),
    Element(number= 81, symbol= "Tl", name= "Thallium", boilingPoint= 1746, meltingPoint= 577, mass= 200.59),
    Element(number= 82, symbol= "Pb", name= "Lead", boilingPoint= 2023, meltingPoint= 600.65, mass= 204.383),
    Element(number= 83, symbol= "Bi", name= "Bismuth", boilingPoint= 1837, meltingPoint= 544.59, mass= 207.2),
    Element(number= 84, symbol= "Po", name= "Polonium", boilingPoint= 1235, meltingPoint= 527.7, mass= 208.9804),
    Element(number= 85, symbol= "At", name= "Astatine", boilingPoint= 610, meltingPoint= 575, mass= 209),
    Element(number= 86, symbol= "Rn", name= "Radon", boilingPoint= 211.4, meltingPoint= 202, mass= 210),
    Element(number= 87, symbol= "Fr", name= "Francium", boilingPoint= 950, meltingPoint= 300, mass= 222),
    Element(number= 88, symbol= "Ra", name= "Radium", boilingPoint= 1413, meltingPoint= 973, mass= 223),
    Element(number= 89, symbol= "Ac", name= "Actinium", boilingPoint= 3470, meltingPoint= 1323, mass= 226.0254),
    Element(number= 90, symbol= "Th", name= "Thorium", boilingPoint= 5060, meltingPoint= 2028, mass= 227),
    Element(number= 91, symbol= "Pa", name= "Protactinium", boilingPoint= 4300, meltingPoint= 1845, mass= 232.0381),
    Element(number= 92, symbol= "U", name= "Uranium", boilingPoint= 4407, meltingPoint= 1408, mass= 231.0359),
    Element(number= 93, symbol= "Np", name= "Neptunium", boilingPoint= 4175, meltingPoint= 912, mass= 238.029),
    Element(number= 94, symbol= "Pu", name= "Plutonium", boilingPoint= 3505, meltingPoint= 913, mass= 237.0482),
    Element(number= 95, symbol= "Am", name= "Americium", boilingPoint= 2880, meltingPoint= 1449, mass= 244),
    Element(number= 96, symbol= "Cm", name= "Curium", boilingPoint= 3383, meltingPoint= 1618, mass= 243),
    Element(number= 97, symbol= "Bk", name= "Berkelium", boilingPoint= 2900, meltingPoint= 1259, mass= 247),
    Element(number= 98, symbol= "Cf", name= "Californium", boilingPoint= 1745, meltingPoint= 1173, mass= 247),
    Element(number= 99, symbol= "Es", name= "Einsteinium", boilingPoint= 1269, meltingPoint= 1133, mass= 251),
    Element(number= 100, symbol= "Fm", name= "Fermium", boilingPoint= "Unknown", meltingPoint= 1800, mass= 252),
    Element(number= 101, symbol= "Md", name= "Mendelevium", boilingPoint= "Unknown", meltingPoint= 1100, mass= 257),
    Element(number= 102, symbol= "No", name= "Nobelium", boilingPoint= "Unknown", meltingPoint= 1100, mass= 258),
    Element(number= 103, symbol= "Lr", name= "Lawrencium", boilingPoint= "Unknown", meltingPoint= 1900, mass= 259),
    Element(number= 104, symbol= "Rf", name= "Rutherfordium", boilingPoint= 5800, meltingPoint= 2400, mass= 262),
    Element(number= 105, symbol= "Db", name= "Dubnium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 261),
    Element(number= 106, symbol= "Sg", name= "Seaborgium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 262),
    Element(number= 107, symbol= "Bh", name= "Bohrium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 263.1182),
    Element(number= 108, symbol= "Hs", name= "Hassium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 264),
    Element(number= 109, symbol= "Mt", name= "Meitnerium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 278),
    Element(number= 110, symbol= "Ds", name= "Darmstadtium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 278),
    Element(number= 111, symbol= "Rg", name= "Roentgenium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 282),
    Element(number= 112, symbol= "Cn", name= "Copernicium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 284),
    Element(number= 113, symbol= "Nh", name= "Nihonium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 288),
    Element(number= 114, symbol= "Fl", name= "Flerovium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 293),
    Element(number= 115, symbol= "Mc", name= "Moscovium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 289),
    Element(number= 116, symbol= "Lv", name= "Livermorium", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 299),
    Element(number= 117, symbol= "Ts", name= "Tennessine", boilingPoint= 883, meltingPoint= "ca. 623-823", mass= 302),
    Element(number= 118, symbol= "Og", name= "Oganesson", boilingPoint= "Unknown", meltingPoint= "Unknown", mass= 294)]

        
   
