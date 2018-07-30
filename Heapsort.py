#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 20:42:08 2018

@author: wenqisun
"""

from timeit import default_timer as timer
import random

testArray1 = random.sample(range(60000),50000)

Arr = [98,14,55,31,44,83,25,77,47,57,49,52,72,29,64,26,33,89,38,32,94,17]

class Heap:
    def __init__(self, alist=[]):
        self.array = alist[:]
        self.array.insert(0,-1)
        self.sort()
            
    def insert(self, data):
        self.array.append(data)
        self.sort()
        
    def sort(self):
        for i in range(int((len(self.array)-1)/2), 0, -1):
            k = i
            v = self.array[k]
            heap = False
            while not heap and 2*k<len(self.array):
                j = 2*k
                if j < len(self.array)-1:
                    if self.array[j] < self.array[j+1]:
                        j = j+1
                if v >= self.array[j]:
                    heap = True
                else:
                    self.array[k] = self.array[j]
                    k = j
            self.array[k] = v
                      
    def eject(self):
        self.array[1], self.array[-1] = self.array[-1], self.array[1]
        output = self.array.pop()
        if len(self.array)>1:
            heap = False
            k = 1
            v = self.array[k]
            while not heap and 2*k<len(self.array):
                j = 2*k
                if j < len(self.array)-1:
                    if self.array[j] < self.array[j+1]:
                        j = j+1
                if v >= self.array[j]:
                    heap = True
                else:
                    self.array[k] = self.array[j]
                    k = j
            self.array[k] = v
        return output
    
    def heapsort(self):
        sortarray = list()
        while len(self.array)>2:
            sortarray.append(self.eject())
        return sortarray

start1 = timer()
myHeap = Heap(testArray1)                 
myHeap.heapsort()
end1 = timer()
print(end1-start1)

        
    
            
    
        