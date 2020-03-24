"""
author: NRG
"""
"""
If you want to get your answers written cleaner, use this in console: %precision %.4e
"""
from math import cos, radians, sqrt

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
u : Atomic mass unit (mass at atomic levels)
mn: Mass neutron. In u
mp: Mass proton. In u

Banelengde: total flytting
Forflyttning: arealet under grafen
Strekning: samme som forflyttning
Posisjon: der du er

Hastighet har retning det har ikke fart
Luftmotstand: k*v^2
"""
c,cv,h,B,u,mn,mp = 3e8, 0.751*3e8, 6.63e-34, 2.18e-18, 1.66e-27, 1.00866491595, 1.007825032241
WIENS = 2.9e-3
"""
The energy level of a given electron shell (in Bohr's atomic model) for a hydrogen atom
"""
def eHyd(shell): return - B / shell**2 #available through website

"""
Calculates energy needed to exitate or deexitate the current electron shell,
where n1 is the starting shell, and n2 is the ending shell.
"""
def eHydDiff(start, end): return abs(eHyd(end)-eHyd(start)) #available through website

"""
Uses time to divide waves by time and get the frequency of a wave.
"""
def freqOld(T, S=1): return S/T #next

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
This function is the same as freq, as they both divide param2 by param1, but it would be confusing to merge them
"""
def wl(f, v=c): return v/f

"""
Plugs c=λf into E=hf to get E=hc/λ
"""
def el(λ): return (h*c)/λ #available through website

"""
Gives energy amount by using Einstein's formula given mass and lightspeed squared
"""
def einstein(m): return m*(c**2) 

"""
Converts u to kg, m = mass in u
"""
def massConvU(m): return m*u 

"""
Gives the leftover energy for a reaction. This energy is freed under the reaction. Takes before mass and subtracts the after mass. Caution! gives energy in u!
"""
def massLeft(before, after): return before-after 

"""
Converts kg to u, m = mass in kg
"""
def massConvKg(m): return m/u

"""
Gets the wavelength of the photon with the given energy
"""
def photonWl(energy):
    f = energy/h
    return wl(f,c)

"""
Calculates the energy of a given photon based on either its wavelength or frequency
"""
def photonEnergy(f= "",wl = ""):
    if f == "" and wl == "": return "Insufficient data"
    if f == "": f = freq(wl)
    return f*h

def kineticEnergy(m,v): return (1/2)*m*(v**2)

def potentialEnergy(m, h, g = 9.81): return m*g*h

def effect(m,g,h,t): return (m*g*h)/t #or arbeid(kraft)/t

def efficiency(n,u): return n/u

def work(F,s,a = 0): return (F*s*cos(radians(a)))

def endVelocity(m,bh,ah,v,f=0,s=0,a=0,g = 9.81): return sqrt(((((potentialEnergy(m,bh)+kineticEnergy(m,v))+work(f,s,a))-potentialEnergy(m,ah))/0.5)/m)

def kmToMps(km): return km/3.6

def mpsToKm(mps): return mps*3.6

def wfl(temp): return temp/WIENS

print('This is a modified Python Console made for Physics 1')
print('The following constants have been defined:')
print(f'c : {c}\ncv : {cv}\nh : {h}\nB : {B}\nu : {u}')
