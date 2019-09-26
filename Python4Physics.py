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
u : Atomic mass unit (mass at atomic levels)
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


"""
Returns in the form of a string the electon configuration of the various orbitals.
While technically lernt in chemistry, this is relevant in all the natural sciences.
Takes electron count (ec), and whether to shorten the result with the last noble gas (short)

⁰¹²³⁴⁵⁶⁷⁸⁹
Some examples to help me think
 1: 1s¹
 2: 1s²
 3: 1s²2s¹
 4: 1s²2s²
 5: 1s²2s²2p¹
 6: 1s²2s²2p²
 7: 1s²2s²2p³
 8: 1s²2s²2p⁴
 9: 1s²2s²2p⁵
10: 1s²2s²2p⁶
11: 1s²2s²2p⁶3s¹
12: 1s²2s²2p⁶3s²
13: 1s²2s²2p⁶3s²3p¹
14: 1s²2s²2p⁶3s²3p²
15: 1s²2s²2p⁶3s²3p³
16: 1s²2s²2p⁶3s²3p⁴
17: 1s²2s²2p⁶3s²3p⁵
18: 1s²2s²2p⁶3s²3p⁶
19: 1s²2s²2p⁶3s²3p⁶4s¹
20: 1s²2s²2p⁶3s²3p⁶4s²
21: 1s²2s²2p⁶3s²3p⁶4s²3d¹
...
30: 1s²2s²2p⁶3s²3p⁶4s²3d¹⁰
31: 1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p¹
36: 1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶
37: 1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s¹
"""
def electronConfig(ec, short=False):
    
    orbitalNames  = ["s","p","d","f"]
    
    
    # Hard coding in the first electron to give the loop a nice start
    shells = [(0,0,1)]
    
    # Iterating over the rest to add them
    for i in range(ec - 1):
        if shells[-1][2] != (4 * shells[-1][1] + 2): # Last subshell isn't full
            # Add one electron to the last shell. Weird because Python doesn't like editing tuple items
            shells[-1] = (shells[-1][0], shells[-1][1], shells[-1][2] + 1)
            # Basically shells[-1][2] += 1
        else:
            # Create new shell
            
            lastShellEnergy = shells[-1][0] + shells[-1][1]
            
            # The toBeat variable will be changed on every iteration of the inner loop if the shell-subshell sum is lower
            # Initialized with an arbitrary large value that will be beaten on the first iteration. 
            # If (100,100) is seen outside of these two lines, something is very wrong.
            toBeat = (100, 100)
            # Loop over the first to last possible shell
            for m in range(1, lastShellEnergy + 2):
                # Loop over subshells
                for s in range(m + 1):
                    # If the subshell we're checking is lower energy than toBeat, replace toBeat.
                    if (m + s) < (toBeat[0] + toBeat[1]) or (((m + s) == (toBeat[0] + toBeat[1])) and m < toBeat[0]):
                        # If the supposedly lower energy shell is actually different from the last
                        for (om, os, _) in shells: 
                            if (om == m and os == s): 
                                print(m,s)
                                continue
                        toBeat = (m,s)
                         
                    
            print()        
            
            shells.append((toBeat[0],toBeat[1],1))    
            
    
    # Turn shells into a string

    return shells

print('This is a modified Python Console made for Physics 1')
print('The following constants have been defined:')
print(f'c : {c}\ncv : {cv}\nh : {h}\nB : {B}')
