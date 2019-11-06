from Elements import *

def find_number_of_particles(grams, atom_number):
    return grams / elements[atom_number].mass  #N = g / Mm

def find_grams_from_number_of_particles(particles, atom_number):
    return particles * elements[atom_number].mass   #g = N * Mm

def massFromFormula(formula):
    if formula == "": return 0  #stop recursion
    if formula[0] == "(": #check parenthesis in formula
        return int(formula[formula.index(")")+1:]) * massFromFormula(formula[1:formula.index(")")]) #find the total mass of the items within the parenthesis
    i = 1  #initialize loop variable
    while (i < len(formula) and not formula[i].isupper()): #find the index of the next atom
        if formula[i] == "(": break  #fix a small problem if the formula contains a parenthesis
        i += 1  #loop through the formula
    expression = formula[:i]  #assign a variable to the first atom and the amount of it
    j = 1  #initialize another loop variable
    while (j < len(expression) and not formula[j].isdigit()): j += 1  #find the index of the first number in the expression
    count = int(expression[j:] if expression[j:] != "" else 1) #find the number of a specific atom
    mass = elements[indexBySymbol(expression[:j])].mass #find the mass per atom for that atom
    return float(count) * mass + massFromFormula(formula[i:]) #using recursion and adding the mass of one atom times the number of that atom
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
