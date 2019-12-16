#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:16:29 2019

@author: victorapeland
"""

import Python4Physics

# Usage: use the factor you want as the function name and type in the three values you already have as parameters. Don't enter the ones you don't have

def velocity(startV=None, a=None, dt=None, ds=None):
    if None not in [startV,a,dt] : return startV + a * dt # Formula 1
    if None not in [dt,startV,ds]: return (ds/((1/2)*dt))-startV
    if None not in [a,ds,startV]  : return (2*a*ds + startV**2)**(1/2) # Can also be negative this.
    print("Insufficient data given.")
    if startV == None:
        print("Trying again assuming startV is 0. If it is not, you will get the wrong answer.")
        return endVelocity(startV=0, a=a, dt=dt, ds=ds)
    if a == None:
        print("Trying again assuming a is 9.81. If it is not, you will get the wrong answer.")
        return endVelocity(startV=startV, a=9.81, dt=dt, ds=ds)
    
def time(startV=None, endV=None,  a=None, ds=None):
    if None not in [startV,endV, a]: return (endV - startV)/a
    if None not in [endV,startV,ds]: return 2*ds/(startV + endV)
    if None not in [startV,a,ds]: 
        sqrt = startV**2 + 2*a*ds
        if sqrt >= 0:
            value1 = (startV + sqrt**(1/2))/a
            value2 = (startV - sqrt**(1/2))/a # TODO: find some way to determine which value is relevant
            return value1
    print("Insufficient data given.")
    if startV == None:
        print("Trying again assuming startV is 0. If it is not, you will get the wrong answer.")
        return time(startV=0, a=a, endV=endV, ds=ds)
    if a == None:
        print("Trying again assuming a is 9.81. If it is not, you will get the wrong answer.")
        return time(startV=startV, a=9.81, endV=endV, ds=ds)
    
def acceleration(startV=None, endV=None, dt=None, ds=None):
    if None not in [endV, startV, dt]: return (endV - startV) / dt
    if None not in [ds, startV, dt]: return 2 * (ds - startV * dt) / dt ** 2
    if None not in [startV, endV, ds]: return (endV ** 2 - startV ** 2) / (2 * ds)
    print("Insufficient data given.")
    if startV == None:
        print("Trying again assuming startV is 0. If it is not, you will get the wrong answer.")
        return acceleration(startV=0, endV=endV, dt=dt, ds=ds)
    
def distance(startV=None, a=None, endV=None, dt=None):
    if None not in [startV, endV, dt]: return 1/2 * dt * (startV + endV) 
    if None not in [a, startV, dt]: return (2*startV*dt + a * dt**2)/2
    if None not in [startV, endV, a]: return (startV ** 2 - endV ** 2) / (2 * a)
    print("Insufficient data given.")
    if startV == None:
        print("Trying again assuming startV is 0. If it is not, you will get the wrong answer.")
        return distance(startV=0, a=a, endV=endV, dt=dt)
    if a == None:
        print("Trying again assuming a is 9.81. If this is not correct, the answer will be wrong.")
        return distance(startV=startV, a=9.81, endV=endV, dt=dt)

def startVelocity(a=None, endV=None, dt=None, ds=None):
    if None not in [a, endV, dt]: return endV - a * dt
    if None not in [ds, endV, dt]: return (2 * ds - dt * endV)/dt
    if None not in [ds, endV, a]: return (endV ** 2 - 2 * a * ds) ** (1/2) # Can also be negative this.
    if None not in [ds, dt, a]: return (2*ds - a * dt**2)/(2*dt)
    print("Insufficient data given.")
    if a == None:
        print("Trying again assuming a is 9.81. If this is not correct, the answer will be wrong.")
        return startVelocity(a=9.81, endV=endV, dt=dt, ds=ds)


# If you want the straight formulae without any funny business, here you go:
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

print()
print("----Motion-py----")
print("The defined formulae are as follows: ")
print("velocity")
print("time")
print("acceleration")
print("distance")
print("startVelocity")
print("With the following parameter names: startV, endV, a, dt, ds")
print()
