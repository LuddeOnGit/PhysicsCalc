from Elements import *
from Subscript import *

numbers = '0123456789'

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
    #Takes the first reactant weight in gram and name, second reactant weight in gram and name and after weight.
    
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
                return f"{elements[fReactNum].symbol}{subscriptString(int(round(fMol, 0)))}{elements[sReactNum].symbol}{subscriptString(int(round(sMol, 0)))}"
    else:
        fMol/= sMol
        sMol = 1
        while True:
            if abs(fMol - round(fMol)) > delta:
                sMol *= 1.1
                fMol *= 1.1
            else:
                return f"{elements[fReactNum].symbol}{subscriptString(int(round(fMol, 0)))}{elements[sReactNum].symbol}{subscriptString(int(round(sMol, 0)))}"

# Takes temperature (°C), difference in Enthalpy (KJ/mol), and difference in Enthropy (J/mol*K). 
# Gives whether the reaction with the given parameters is spontaneous.
def isSpontaneous(temp, dH, dS): return dH - toK(temp) * dS / 1000 < 0

# Takes temperature (°C), difference in Enthalpy (KJ/mol), and difference in Enthropy (J/mol*K). 
# Gives the value in kJ
def gibbsValue(temp, dH, dS): return dH - toK(temp) * dS / 1000

def enthalpy(testIn, justVal = False):
    reactants = testIn.split(" = ")
    product = reactants.pop()
    reactants = reactants[0].split(" + ")
    product = product.split(" + ")
    
    sumReactants = enthalpySumReact(reactants)
    sumProduct = enthalpySumProd(product)
    dH = round(sumProduct-sumReactants,2)
    if justVal != True:
        return f"The reaction is endothermic with the ΔH value: {dH}" if dH > 0 else f"The reaction is exothermic with the ΔH value: {dH}"
    else:
        return dH
    
def enthalpySumReact(reactants):
    endSum = 0
    cof = 1
    for i in range(len(reactants)):
        split = reactants[i].rfind("(")
        
        if reactants[i][0] in numbers:
            for t in range(len(reactants[i][:+4])):
                if reactants[i][t] not in numbers:
                    break
            cof = int(reactants[i][:t])
        
        for j in range(len(STV)):
            if STV[j].formula == reactants[i][t:split] and STV[j].state == reactants[i][split+1:-1]:
                endSum += cof*STV[j].dEnthalpy
                break
    return endSum
    
def enthalpySumProd(product):
    endSum = 0
    cof = 1
    for i in range(len(product)):
        split = product[i].rfind("(")

        if product[i][0] in numbers:
            for t in range(len(product[i][:+4])):
                if product[i][t] not in numbers:
                    break
            cof = int(product[i][:t])
        
        for j in range(len(STV)):
            if STV[j].formula == product[i][t:split] and STV[j].state == product[i][split+1:-1]:
                endSum += cof*STV[j].dEnthalpy
                break
    return endSum

def entropy(testIn, justVal = False):
    reactants = testIn.split(" = ")
    product = reactants.pop()
    reactants = reactants[0].split(" + ")
    product = product.split(" + ")
    
    sumReactants = entropySumReact(reactants)
    sumProduct = entropySumProd(product)
    dS = round(sumProduct-sumReactants,2)
    if justVal != True:
        return f"The reaction gets more caotic with the ΔS value: {dS}" if dS > 0 else f"The reaction gets less chaotic with the ΔS value: {dS}"
    else: 
        return dS
    
def entropySumReact(reactants):
    endSum = 0
    cof = 1
    for i in range(len(reactants)):
        split = reactants[i].rfind("(")
        
        if reactants[i][0] in numbers:
            for t in range(len(reactants[i][:+4])):
                if reactants[i][t] not in numbers:
                    break
            cof = int(reactants[i][:t])
        
        for j in range(len(STV)):
            print(reactants[i][:split])
            if STV[j].formula == reactants[i][t:split] and STV[j].state == reactants[i][split+1:-1]:
                endSum += cof*STV[j].dEntropy
                break
    return endSum
    
def entropySumProd(product):
    endSum = 0
    cof = 1
    for i in range(len(product)):
        split = product[i].rfind("(")
        
        if product[i][0] in numbers:
            for t in range(len(product[i][:+4])):
                if product[i][t] not in numbers:
                    break
            cof = int(product[i][:t])
        
        for j in range(len(STV)):
            if STV[j].formula == product[i][t:split] and STV[j].state == product[i][split+1:-1]:
                endSum += cof*STV[j].dEntropy
                break
    return endSum

def gibbsFull(testIn, temp = 25): return gibbsValue(temp, enthalpy(testIn, True), entropy(testIn, True))