#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:16:29 2019

@author: victorapeland
"""


def endVelocity(startV="", a="", dt="", ds=""):
    if "" not in [startV,a,dt] : return startV + a * dt # Formula 1
    if "" not in [dt,startV,ds]: return startV - 2*ds/dt
    if "" not in [a,ds,startV]  : return (2*a*ds - startV**2)**(1/2)
    return "no"
    

def time(startV="", endV="",  a="", ds=""):
    if "" not in [startV,endV, a]: return (endV - startV)/a
    if "" not in [endV,startV,ds]: return ds/((startV + endV)/2)
    if "" not in [startV,a,ds]: 
        sqrt = startV**2 + 2*a(ds)
        if sqrt < 0: return
        value1 = (startV + sqrt**(1/2))/a
        value2 = (startV - sqrt**(1/2))/a # TODO: find some way of determinint which value is relevant
        return value1
    

        
def beginning_velocity(ds="", a="", endV="", dt=""):
    if "" not in [a, endV, dt]: return endV - a * dt
    if "" not in [ds, endV, dt]: return 2 * ds / dt - endV
    if "" not in [ds, endV, a]: return (endV * 2 - 2 * a * ds) * (1/2)
    return "You noob!!"   

def acceleration(startV="", endV="", dt="", ds=""):
    if "" not in [endV, startV, dt]: return (endV - startV) / dt
    if "" not in [ds, startV, dt]: return 2 * (ds - startV * dt) / dt ** 2
    if "" not in [startV, endV, ds]: return (endV * 2 - startV * 2) / (2 * ds)
    
def distance(startV="", a="", endV="", dt=""):
    if "" not in [startV, endV, dt]: return 1/2 * dt * (startV + endV) 
    if "" not in [a, startV, dt]: return startV * dt + 1/2 * a * dt ** 2
    if "" not in [startV, endV, a]: return (startV * 2 - endV * 2) / (2 * a)
    return "You noob!!"

def startVelocity(ds="", a="", endV="", dt=""):
    if "" not in [a, endV, dt]: return endV - a * dt
    if "" not in [ds, endV, dt]: return 2 * ds / dt - endV
    if "" not in [ds, endV, a]: return (endV * 2 - 2 * a * ds) * (1/2)
    return "You noob!!"

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
