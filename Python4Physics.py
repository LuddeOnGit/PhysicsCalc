"""
author: NRG
"""
"""
If you want to get your answers written cleaner, use this in console: %precision %.4e
"""
from Elements import *
from GUI import *

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
"""
c,cv,h,B,u,mn,mp = 3e8, 0.751*3e8, 6.63e-34, 2.18e-18, 1.66e-27, 1.00866491595, 1.007825032241

"""
The energy level of a given electron shell (in Bohr's atomic model) for a hydrogen atom
"""
def eHyd(shell): return - B / shell**2

"""
Calculates energy needed to exitate or deexitate the current electron shell,
where n1 is the starting shell, and n2 is the ending shell.
"""
def eHydDiff(n1,n2): return abs(eHyd(n1)-eHyd(n2))

"""
Uses time to divide waves by time and get the frequency of a wave.
"""
def freqOld(T, S=1): return S/T

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
def mass(m, v=c): return m*(v**2) #GUI done

"""
Converts u to kg, m = mass in u
"""
def massConvU(m): return m*u #GUI done

"""
Gives the leftover energy for a reaction. This energy is freed under the reaction. Takes before mass and subtracts the after mass. Caution! gives energy in u!
"""
def massLeft(before, after): return before-after #GUI done

"""
Converts kg to u, m = mass in kg
"""
def massConvKg(m): return m/u #GUI done

"""
Gets the wavelength of the photon with the given energy
"""
def wlPhoton(energy): #GUI done
    f = energy/h
    return wl(f,c)

"""
Calculates final speed from known start speed, acceleration and time from start to end
"""
def first_equation_of_motion(v_start, a, delta_time):
    return v_start + a * delta_time

"""
Calculates length something has moved from known start speed, end speed and time from start to end
"""
def second_equation_of_motion(v_start, v_end, delta_time):
    return delta_time/2 * (v_start+v_end)

"""
Calculates length something has moved from known start speed, time from start to end and acceleration 
"""
def third_equation_of_motion(v_start, delta_time, a):
    return v_start * delta_time + (1/2) * a * delta_time ** 2

"""
"Timeless formula" Calculates the value of 2 * acceleration * end position from known start speed and end speed
"""
def fourth_equation_of_motion(v_start, v_end):
    return v_end ** 2 - v_start ** 2

print('This is a modified Python Console made for Physics 1')
print('The following constants have been defined:')
print(f'c : {c}\ncv : {cv}\nh : {h}\nB : {B}\nu : {u}')
