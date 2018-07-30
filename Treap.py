#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 13:15:14 2018

@author: wenqisun
"""

import copy

class Treap:
    def __init__(self, node):
        self.val = node[0]
        self.priority = node[1]
        self.left = None
        self.right = None
        
    def __str__(self):
        return '<%s, (%s%d), %s>' % (self.left, self.val, self.priority ,self.right)
    
def insert(item, treap):
    if item[0] < treap.val:
        if treap.left is None:
            treap.left = Treap(item)
        else:
            insert(item, treap.left)
    else:
        if treap.right is None:
            treap.right = Treap(item)
        else:
            insert(item, treap.right)

def rotate(treap):
    if treap.left != None:
        treap.left = rotate(treap.left)
        if treap.priority > treap.left.priority:
            return rightRotate(treap)
    if treap.right != None:
        treap.right = rotate(treap.right)
        if treap.priority > treap.right.priority:
            return leftRotate(treap)
    return treap

def rightRotate(treap):
    leftTreap = copy.deepcopy(treap.left)
    treap.left = copy.deepcopy(leftTreap.right)
    leftTreap.right = copy.deepcopy(treap)
    return copy.deepcopy(leftTreap)

def leftRotate(treap):
    rightTreap = copy.deepcopy(treap.right)
    treap.right = copy.deepcopy(rightTreap.left)
    rightTreap.left = copy.deepcopy(treap)
    return copy.deepcopy(rightTreap)

def BuildTreap(L):
    treap = Treap(L[0])
    for i in range(1,len(L)):
        insert(L[i], treap)
        treap = rotate(treap)
    return treap

#treap = BuildTreap([('a',9),('b',3),('c',7),('d',2),('e',6),('f',5),('g',4)])
#print(treap)