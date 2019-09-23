"""
Created on Thu Sep 19 10:44:08 2019

@author: Ludvik Fjeld
"""

# SI prefixes
"""
Usage:
Replace your exponent with the corresponding prefix. For example:
2.18e-18 --> 2.18*E

Doesn't really save space, but it's nice to have them here so you don't have to look 'em up.
"""
a,f,p,n,µ,m,c,d,da,he,k,M,G,T,P,E = e-18,e-15,e-12,e-9,e-6,e-3,e-2,e-1,e1,e2,e3,e6,e9,e12,e15,e18

# Physical constants.
"""
c : The speed of light in a vacuum. In m/s
cv: The speed of light in water. In m/s
h : Planck constant. In Js
B : Bohr's constant. In J
""""
c,cv,h,B = 3e8, 0.751*3e8, 6.63e-34, 2.18e-18

"""
The energy level of a given electron shell (in Bohr's atomic model) for a hydrogen atom
"""
def eHyd(shell): return - B / shell**2

"""
Calculates energy needed to exitate or deexitate the current electron shell,
where n1 is the starting shell, and n2 is the ending shell.
"""
def eHydDiff(n1,n2): return eHyd(n2)-eHyd(n1)


"""
Calculates wave speed by multiplying wavelength(λ) by frequency(f)
"""
def speed(λ, f): return λ*f

"""
Calculates Frequency by dividing speed of the wave(c or other if that is specified) by wavelength(λ)
"""
def freq(λ, speed=c): return speed/λ

"""
Calculates wavelength(λ) by dividing the speed of the wave(speed, implicitly c) by frequency(f)
"""
def wl(f, speed=c): return speed/f

"""
Calculates Energy of a given photon with frequency f. 
Takes Plancks-constant(h) and frequency(f)
"""
def e(f): return h*f


print('This is a modified Python Console made for Physics 1')
print('The following constants have been defined:')
print(f'c : {c}\ncv : {cv}\nh : {h}\nB : {B}')
