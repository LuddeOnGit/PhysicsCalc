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
a,f,p,n,µ,m,c,d,da,he,k,M,G,T,P,E = 1e-18,1e-15,1e-12,1e-9,1e-6,1e-3,1e-2,1e-1,1e1,1e2,1e3,1e6,1e9,1e12,1e15,1e18

# Physical constants.
"""
c : The speed of light in a vacuum. In m/s
cv: The speed of light in water. In m/s
h : Planck constant. In Js
B : Bohr's constant. In J
u = atomic mass unit (mass at atomic levels)
"""
c,cv,h,B, u = 3e8, 0.751*3e8, 6.63e-34, 2.18e-18, 1.66e-27

"""
The energy level of a given electron shell (in Bohr's atomic model) for a hydrogen atom
"""
def eHyd(shell): return - B / shell**2

"""
Calculates energy needed to exitate or deexitate the current electron shell,
where n1 is the starting shell, and n2 is the ending shell.
"""
def eHydDiff(n1,n2): return eHyd(n1)-eHyd(n2)


"""
Calculates wave speed by multiplying wavelength(λ) by frequency(f)
"""
def speed(λ, f): return λ*f

"""
Calculates Frequency by dividing speed of the wave(c or other if that is specified) by wavelength(λ)
"""
def freq(λ, v=c): return v/λ

"""
Calculates wavelength(λ) by dividing the velocity of the wave(v, implicitly c) by frequency(f)
"""
def wl(f, v=c): return v/f

"""
Calculates Energy of a given photon with frequency f. 
Takes Plancks-constant(h) and frequency(f)
"""
def ef(f): return h*f

"""
Plugs c=λf into E=hf to get E=hc/λ
"""
def el(λ): return (h*c)/λ

"""
Gives energy amount by using Einstein's formula given mass and lightspeed squared
"""
def mass(m, v=c): return m*(v**2)

"""
converts u to kg, m = mass in u
"""
def massConvU(m): return m*u

"""
Converts kg to kg, m = mass in kg
"""
def massConvKg(m): return m/u

print('This is a modified Python Console made for Physics 1')
print('The following constants have been defined:')
print(f'c : {c}\ncv : {cv}\nh : {h}\nB : {B}')
