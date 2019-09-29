#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:48:25 2019

@author: victorapeland
"""

from tkinter import *
import Elements

def PeriodicTable():
    window = Tk()
    window.title = "Periodic Table"
    
    for element in Elements.elements:
        if type(element.group()) == int:
            label = Label(window, text=element.symbol, font="none 16")
            label.grid(row=element.period(), column=element.group(), sticky=W)

PeriodicTable()
