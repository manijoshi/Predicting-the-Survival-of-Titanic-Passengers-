# -*- coding: utf-8 -*-
"""
Created on Thu May 21 03:19:10 2020

@author: MONIKA JOSHI
"""

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    c=0
    for i in range(n):
        c+=1
    print(c)
fib(100)
