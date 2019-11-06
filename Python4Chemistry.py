from Elements import *

def find_number_of_particles(grams, atom_number):
    return grams / elements[atom_number].mass

def find_grams_from_number_of_particles(particles, atom_number):
    return particles * elements[atom_number].mass

def massFromFormula(formula, amount = 1):
    if formula == "": return 0
    if formula[0] == "(":
        l = formula.index(")")
        content = formula[1:l]
        amount = int(formula[l+1:])
        return massFromFormula(content, amount)
    
    i = 1
    while (i < len(formula) and not formula[i].isupper()):
        if formula[i] == "(": break
        else: i += 1
    
    expression = formula[0:i]
    
    j = 1
    while (j < len(expression) and not formula[j].isdigit()): j += 1
    
    symbol = expression[:j]
    count = int(expression[j:] if expression[j:] != "" else 1) * amount
    
    mass = elements[indexBySymbol(symbol)].mass
    
    return float(count) * mass + massFromFormula(formula[i:], amount)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
