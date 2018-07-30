#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:35:16 2018

@author: wenqisun
"""

graph = [['a',['b','c','d','e']],['b',['a','d','e']],['c',['a']],['d',['a','b','e']],['e',['a','b','d']],['f',['g']],['g',['f']]]

class Queue:
    
    def __init__(self):
        self.queue = list()
        
    def enqueue(self,data):
        self.queue.insert(0,data)
        
    def dequeue(self):
        return self.queue.pop()
        
    def size(self):
        return len(self.queue)


def DFS(graph,visited):
    def Explore(node):
        if node not in visited:
            visited.append(node)
            i = 0
            for i in range(0,len(graph)):
                if graph[i][0] == node:
                    break;
            for j in range(0,len(graph[i][1])):
                if graph[i][1][j] not in visited:
                    Explore(graph[i][1][j])
                    
    for i in range(0,len(graph)):
        Explore(graph[i][0])                                  
    return visited

print(DFS(graph,[]))

def BFS(graph,visited):
    queue = Queue()
    for i in range(0,len(graph)):
        if graph[i][0] not in visited:
            visited.append(graph[i][0])
            queue.enqueue(graph[i][0])
            while queue.size() > 0 :
                node = queue.dequeue()
                k = 0
                for k in range(0,len(graph)):
                    if graph[k][0] == node:
                        break;
                for j in range(0,len(graph[k][1])):
                    if graph[k][1][j] not in visited:
                        visited.append(graph[k][1][j])
                        queue.enqueue(graph[k][1][j])
    return visited

print(BFS(graph,[]))