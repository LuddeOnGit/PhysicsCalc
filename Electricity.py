# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:41:27 2020

@author: Ludvik Fjeld
"""

import math

q = 1.63e-19

def spenning(R,I): return R*I #Volt

def strøm(R,U): return U/R #Ampere

def resistans(I,U): return U/I #Ohm

def totRes(motstander):
    motstander = sum([1/i for i in motstander])
    return 1/motstander

def effect(I,R,U=None):
    if U == None:
        return (I**2)*R
    else:
        return U*I