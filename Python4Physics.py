# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:44:08 2019

@author: Ludvik Fjeld
"""

# SI prefixes
a,f,p,n,µ,m,c,d,da,he,k,M,G,T,P,E = 10e-18,10e-15,10e-12,10e-9,10e-6,10e-3,10e-2,10e-1,10e1,10e2,10e3,10e6,10e9,10e12,10e15,10e18

# Physical constants
c,cv,h,B = 3e8, 0.751*3e8, 6.63e-34, 2.18e-18

"""
Calculates energy needed to exitate or deexitate the current electron shell,
where n1 is the starting shell, and n2 is the ending shell.
"""
def ehyd(n1,n2):
    """
    Joule
    """
    return (-B/n1**2)-(-B/n2**2)

"""
Calculates Frequency by dividing speed of the wave(c or other if that is specified) by wavelength(λ)
"""
def hz(λ, speed=c):
    """
    Hertz
    """
    return speed/λ

"""
Calculates Energy for a given foton. 
Takes Plancks-constant(h) and frequency(f)
"""
def e(f):
    """
    Joule
    """
    return h*f

print('This is a modified Python Console made for Physics 1')
print('The following variables have been defined:')
print(f'c : {c}\ncv : {cv}\nh : {h}\nB : {B}')
