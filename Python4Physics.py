# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:44:08 2019

@author: Ludvik Fjeld
"""

c,cv,h,B = 3e8, 0.751*3e8, 6.63e-34, 2.18e-18
def e(n1,n2):
    return (-B/n1**2)-(-B/n2**2)
def hz(λ):
    return c/λ
print('This is a modified Python Console made for Physics 1')
print('The following variables have been defined:')
print(f'c : {c}\ncv : {cv}\nh : {h}\nB : {B}')