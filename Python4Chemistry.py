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