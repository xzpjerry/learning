#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''
nodes = ('A', 'B', 'C', 'D', 'E')
distances = {
    'A':{'B': 2, 'E': 20},
    'B':{'E': 21, 'C':2},
    'C':{'E': 22, 'D': 2},
    'D':{'E': 23},
    'E':{}
    }

def dj_shortest(nodes, distances, start):
    unvisted = {node: None for node in nodes}
    #{'C': None, 'B': None, 'A': None}
    visted = {}
    current = start
    current_dis = 0
    unvisted[current] = current_dis
    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisted: continue
            new_dist = current_dis + distance
            if unvisted[neighbour] == None or unvisted[neighbour] > new_dist:
                unvisted[neighbour] = new_dist
        visted[current] = current_dis
        del unvisted[current]
        if not unvisted: break
        rest_of_them = [node for node in unvisted.items() if node[1]]
        current, current_dis = sorted(rest_of_them, key = lambda x: x[1])[0]
    print(visted)

dj_shortest(nodes, distances, 'A')
