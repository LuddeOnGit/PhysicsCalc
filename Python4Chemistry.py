from Elements import *

def find_number_of_particles(grams, atom_number):
    return grams / elements[atom_number].mass

def find_grams_from_number_of_particles(particles, atom_number):
    return particles * elements[atom_number].mass
    
    
