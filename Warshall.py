#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 12:54:12 2018

@author: wenqisun
"""
import copy

def Warshall(L):
    length = len(L)
    R = []
    R.append(copy.deepcopy(L))  #list is mutable
    for k in range(1, length+1):
        for i in range(0, len(L)):
            for j in range(0, len(L)):
                L[i][j] = (R[k-1][i][j] or (R[k-1][i][k-1] and R[k-1][k-1][j]))
        R.append(copy.deepcopy(L))
    return R[k]

def Floyd(L):
    for k in range(1, len(L)+1):
        for i in range(0, len(L)):
            for j in range(0, len(L)):
                L[i][j] = min(L[i][j], L[i][k-1]+L[k-1][j])
    return L

#test = [[0,math.inf,3,math.inf],[2,0,math.inf,math.inf],[math.inf,7,0,1],[6,math.inf,math.inf,0]]
#print(Floyd(test))

def Warshall_ver2(L):
    for k in range(1, len(L)+1):
        for i in range(0, len(L)):
            for j in range(0, len(L)):
                L[i][j] = L[i][j] or (L[i][k-1] and L[k-1][j])
    return L

#test1 = [[0,1,0,0],[0,0,0,1],[0,0,0,0],[1,0,1,0]]
#print(Warshall_ver2(test1))

test2 = [[0,3],[-4,0]]
print(Floyd(test2))