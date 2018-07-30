#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:56:03 2018

@author: wenqisun
"""

import math
from timeit import default_timer as timer
import random

testArray1 = random.sample(range(600000),500000)
testArray2 = testArray1.copy()
testArray3 = testArray1.copy()
testArray4 = testArray1.copy()
testArray5 = testArray1.copy()
testArray6 = testArray1.copy()

def SelSort(L):
    for i in range(0, len(L)-1):
        min = L[i],i
        for j in range(i+1, len(L)):
            if L[j] < min[0]:
                min = L[j],j
        temp = L[i]
        L[i] = min[0]
        L[min[1]] = temp
    return L


def InsertionSort(L):
    for i in range(1,len(L)):
        v = L[i]
        j = i-1
        while (j>=0 and v<L[j]):
            L[j+1] = L[j]
            j -= 1
        L[j+1] = v

#start1 = timer()
#InsertionSort(testArray1)
#end1 = timer()
#print(end1-start1)


def ShellSort(L,gap):
    for i in range(0,gap):
        for j in range(i+gap,len(L),gap):
            v = L[j]
            k = j-gap
            while (k>=0 and v<L[k]):
                L[k+gap] = L[k]
                k -= gap
            L[k+gap] = v

#start2 = timer()
#ShellSort(testArray2,1093)
#ShellSort(testArray2,364)
#ShellSort(testArray2,121)
#ShellSort(testArray2,40)
#ShellSort(testArray2,13)
#ShellSort(testArray2,4)
#ShellSort(testArray2,1)
#end2 = timer()
#print(end2-start2)


def MergeSort(L):
    def Merge(sub1,sub2,final):
        i, j, k = 0, 0, 0
        while (i<len(sub1) and j<len(sub2)):
            if sub1[i] <= sub2[j]:
                final[k] = sub1[i]
                i += 1
            else:
                final[k] = sub2[j]
                j += 1
            k += 1
        if i == len(sub1):
            for m in range(j, len(sub2)):
                final[k] = sub2[m]
                k += 1
        else:
            for m in range(i, len(sub1)):
                final[k] = sub1[m]
                k += 1
    if len(L)>1:
        A = L[:math.floor(len(L)/2)].copy()
        B = L[math.floor(len(L)/2):].copy()
        MergeSort(A)
        MergeSort(B)
        Merge(A,B,L)
 
#start3 = timer()       
#MergeSort(testArray3)
#end3 = timer()
#print(end3-start3)

def QuickSort(L):
    def _quicksort(alist, low, high):
        if low < high:
            p = Partition(alist, low, high)
            _quicksort(alist, low, p)
            _quicksort(alist, p+1, high)
    
    def Partition(alist, low, high):
        i = low
        j = high
        pivot = L[i]
        while i < j:
            while i < high and L[i] <= pivot:
                i += 1
            while j >= low and L[j] > pivot:
                j -= 1
            L[i], L[j] = L[j], L[i]
        L[i], L[j] = L[j], L[i]
        L[low], L[j] = L[j], L[low]
        return j
    
    _quicksort(L, 0, len(L)-1)

#start4 = timer()
#QuickSort(testArray4)
#end4 = timer()
#print(end4-start4)

def AdvancedQuickSort(L):
    def _quickalmostsort(alist, low, high):
        if low+10 < high:
            p = Partition(alist, low, high)
            _quickalmostsort(alist, low, p)
            _quickalmostsort(alist, p+1, high)
            
    def Partition(alist, low, high):
        median = [alist[low], alist[math.floor((low+high)/2)], alist[high]]
        median.sort()
        alist[low] = median[1]
        alist[math.floor((low+high)/2)] = median[0]
        alist[high] = median[2]
        pivot = alist[low]
        i, j = low, high
        while i < j:
            while L[i] < pivot:
                i += 1
            while L[j] > pivot:
                j -= 1
            L[i], L[j] = L[j], L[i]
        L[i], L[j] = L[j], L[i]
        L[low], L[j] = L[j], L[low]
        return j
    
    _quickalmostsort(L, 0, len(L)-1)
    InsertionSort(L)

#start5 = timer()
#AdvancedQuickSort(testArray5)
#end5 = timer()
#print(end5-start5)
        
start6 = timer()
testArray1.sort()
end6 = timer()
print(end6-start6)
