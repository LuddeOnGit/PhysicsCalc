#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:41:26 2019

@author: victorapeland
"""

# Two quick functions to subscript numbers using the unicode symbols, for chemical formulae and such. 
# Example Usage:
# from Subscript import *
# print(subscriptString("1234")) # Prints: ₁₂₃₄


def subscriptChar(character):
    if character == "0": return "₀"
    if character == "1": return "₁"
    if character == "2": return "₂"
    if character == "3": return "₃"
    if character == "4": return "₄"
    if character == "5": return "₅"
    if character == "6": return "₆"
    if character == "7": return "₇"
    if character == "8": return "₈"
    if character == "9": return "₉"
    if character == "+": return "₊"
    if character == "-": return "₋"
    if character == "=": return "₌"
    if character == "(": return "₍"
    if character == ")": return "₎"
    
    return character

def subscriptString(string):
    string = str(string) # Make sure in case someone passes an int or something
    ans = ""
    for c in string:
        ans += subscriptChar(c)
        
    return ans