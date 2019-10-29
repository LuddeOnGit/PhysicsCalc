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
        value2 = (startV - sqrt**(1/2))/a
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
