# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:44:08 2019

@author: Ludvik Fjeld
"""

# SI prefixes
a,f,p,n,µ,m,c,d,da,he,k,M,G,T,P,E = e-18,e-15,e-12,e-9,e-6,e-3,e-2,e-1,e1,e2,e3,e6,e9,e12,e15,e18

# Physical constants
c,cv,h,B = 3e8, 0.751*3e8, 6.63e-34, 2.18e-18


def eHyd(shell): return - B / shell**2

"""
Calculates energy needed to exitate or deexitate the current electron shell,
where n1 is the starting shell, and n2 is the ending shell.
"""
def eHydDiff(n1,n2): return eHyd(n1)-eHyd(n2)

"""
Calculates Frequency by dividing speed of the wave(c or other if that is specified) by wavelength(λ)
"""
def hz(λ, speed=c): return speed/λ

"""
Calculates Energy for a given foton. 
Takes Plancks-constant(h) and frequency(f)
"""
def e(f): return h*f


print('This is a modified Python Console made for Physics 1')
print('The following variables have been defined:')
print(f'c : {c}\ncv : {cv}\nh : {h}\nB : {B}')
