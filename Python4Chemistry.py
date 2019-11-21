from Elements import *

def toK(celsius): return celsius + 273.15

def toC(kelvin): return kelvin - 273.15

def find_number_of_particles(grams, atom_number):
    return grams / elements[atom_number].mass  #N = g / Mm

def find_grams_from_number_of_particles(particles, atom_number):
    return particles * elements[atom_number].mass   #g = N * Mm

def massFromFormula(formula):
    if formula == "": return 0  #stop recursion

    # Assumes possible parentheses are at the end of the formula, and that it has a number after it
    if formula[0] == "(": #check for opening parenthesis in formula
        closingIndex = formula.index(")")
        return int(formula[closingIndex+1:]) * massFromFormula(formula[1:closingIndex]) #find the total mass of the items within the parenthesis

    # Seperate the first expression from the rest
    i = 1  #initialize loop variable
    while (i < len(formula) and not formula[i].isupper()): #find the index of the next atom
        if formula[i] == "(": break  #fix a small problem if the formula contains a parenthesis
        i += 1  #loop through the formula
    expression = formula[:i]  #assign a variable to the first atom and the amount of it

    # Seperate the symbol and count
    j = 1  #initialize another loop variable
    while (j < len(expression) and not formula[j].isdigit()): j += 1  #find the index of the first number in the expression
    count = int(expression[j:] if expression[j:] != "" else 1) #find the number of a specific atom
    symbol = indexBySymbol(expression[:j])
    
    mass = elements[symbol].mass #find the mass per atom for that atom
    
    return float(count) * mass + massFromFormula(formula[i:]) #using recursion and adding the mass of one atom times the number of that atom

def empirical(fReactNum, fReactWeight, sReactNum, aWeight, delta = 1/3):
    """
    Takes the first reactant weight in gram and name, second reactant weight in gram and name and after weight.
    """
    
    sReactWeight = aWeight - fReactWeight
    
    fMol = fReactWeight/elements[fReactNum].mass
    sMol = sReactWeight/elements[sReactNum].mass
    
    if fMol < sMol:
        sMol /= fMol
        fMol = 1
        while True:
            if abs(sMol - round(sMol)) > delta:
                sMol *= 1.1
                fMol *= 1.1
            else:
                return f"{elements[fReactNum].symbol}{int(round(fMol, 0))}{elements[sReactNum].symbol}{int(round(sMol, 0))}"
    else:
        fMol/= sMol
        sMol = 1
        while True:
            if abs(fMol - round(fMol)) > delta:
                sMol *= 1.1
                fMol *= 1.1
            else:
                return f"{elements[fReactNum].symbol}{int(round(fMol, 0))}{elements[sReactNum].symbol}{int(round(sMol, 0))}"

# Takes temperature (°C), difference in Enthalpy (KJ/mol), and difference in Enthropy (J/mol*K). 
# Gives whether the reaction with the given parameters is spontaneous.
def isSpontaneous(temp, dH, dS): return dH - toK(temp) * dS / 1000 < 0

# Takes temperature (°C), difference in Enthalpy (KJ/mol), and difference in Enthropy (J/mol*K). 
# Gives the value in kJ
def gibbsValue(temp, dH, dS): return dH - toK(temp) * dS / 1000

class STVFormula:
    
    def __init__(self, formula, state, dEnthalpy, dGibbs, dEntropy):
        self.formula = formula
        self.state = state
        self. dEnthalpy = dEnthalpy
        self.dGibbs = dGibbs
        self.dEntropy = dEntropy

STV = [#formula | state | dEnthalpy | dGibbs | dEntropy |
       STVFormula("Ag","s",0,0,42.55),
       STVFormula("Ag","g",284.55,245.65,172.997),
       STVFormula("Ag(NH3)2^+","aq",-111.29,-17.12,245.2),
       STVFormula("Ag(S2O3)2^3-","aq",-1285.7,-1033.65,98.92),
       STVFormula("Ag^+","aq",105.579,77.107,72.68),
       STVFormula("Ag^+","g",1021.73,None,None),
       STVFormula("Ag2CO3","s",-505.8,-436.8,167.4),
       STVFormula("Ag2CrO4","s",-731.74,-641.76,217.6),
       STVFormula("Ag2O","s",-31.05,-11.2,121.3),
       STVFormula("Ag2S","s",-32.59,-40.67,144.01),
       STVFormula("Ag2SO4","s",-715.88,-618.41,200.4),
       STVFormula("Ag3PO4","s",None,-879,None),
       STVFormula("AgBr","s",-100.37,-96.9,107.1),
       STVFormula("AgCl","s",-127.068,-109.789,96.2),
       STVFormula("AgCl2^-","aq",-245.2,-215.4,231.4),
       STVFormula("AgCN","s",146,156.9,107.19),
       STVFormula("AgCNS","s",87.9,101.39,131),
       STVFormula("AgI","s",-61.83,-66.19,115.5),
       STVFormula("AgNO3","s",-124.39,-33.47,140.92),
       STVFormula("Al","s",0,0,28.33),
       STVFormula("Al","g",326.4,285.7,164.54),
       STVFormula("Al(OH)3","s",-1276,None,None),
       STVFormula("Al2O3","s",-1675.7,-1582.3,50.92),
       STVFormula("Al^3+","aq",-531,-485,-321.7),
       STVFormula("Al^3+","g",5483.17,None,None),
       STVFormula("AlCl3","s",-704.2,-628.8,110.67),
       STVFormula("AlCl3","g",-583.2,None,None),
       STVFormula("Ar","g",0,0,154.843),
       STVFormula("As","s",0,0,35.1),
       STVFormula("B","s",0,0,5.86),
       STVFormula("Ba","s",0,0,62.8),
       STVFormula("Ba^2+","aq",-537.64,-560.77,9.6),
       STVFormula("BaC2O4","s",-1368.6,None,None),
       STVFormula("BaCO3","s",-1216.3,-1137.6,112.1),
       STVFormula("BaCrO4","s",-1446,-1345.22,158.6),
       STVFormula("BaF2","s",-1207.1,-1156.8,96.36),
       STVFormula("BaSo4","s",-1473.2,-1362.2,132.2),
       STVFormula("Be","s",0,0,9.5),
       STVFormula("BeO","s",-609.6,-580.3,14.14),
       STVFormula("BF3","g",-1137,-1120.35,254.01),
       STVFormula("Bi","s",0,0,56.74),
       STVFormula("Bi2S3","s",-143.1,-140.6,200.4),
       STVFormula("Bi^3+","aq",None,82.8,None),
       STVFormula("Br^-","aq",-121.55,-103.96,82.4),
       STVFormula("Br","g",111.88,82.429,174.91),
       STVFormula("Br^-","g",-219.07,None,None),
       STVFormula("Br2","g",30.907,3.11,245.463),
       STVFormula("Br2","l",0,0,152.231),
       STVFormula("Br3^-","aq",-130.42,-107.05,215.5),
       STVFormula("BrO3^-","aq",-67.07,18.6,161.71),
       STVFormula("C","s",0,0,5.74),
       STVFormula("C","g",716.682,671.257,158.096),
       STVFormula("(Ch3)2O","g",-184.05,-112.59,266.38),
       STVFormula("C2H2","g",226.73,209.2,200.94),
       #STVFormula("","",,,), template
       
       ]