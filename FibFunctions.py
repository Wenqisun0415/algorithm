#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:16:20 2018

@author: wenqisun
"""
import math

def Fib_fast(n):
    c1, c2 = math.sqrt(5)/5, -math.sqrt(5)/5
    lambda1, lambda2 = (1+math.sqrt(5))/2, (1-math.sqrt(5))/2;
    result = c1 * pow(lambda1, n+1) + c2 * pow(lambda2, n+1)
    return round(result)

def Fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)
    
def Fib_linear(n, a, b):
    if n == 0:
        return a
    else:
        return Fib_linear(n-1, a+b, a)
    