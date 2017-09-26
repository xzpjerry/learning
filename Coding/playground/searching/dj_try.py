#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''
nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'Z')
distances = {
    'A': {'B': 1, 'E': 7, 'C': 5, 'D': 7},
    'B': {'Z': 8},
    'C': {'G': 2},
    'D': {'F': 5, 'E': 8},
    'E': {'G': 5, 'F': 8},
    'F': {'E': 5, 'G': 7},
    'G': {'Z': 1},
    'Z': {'G': 9}
}


def dj_shortest(nodes, distances, start, target=None):
    unvisted = {node: None for node in nodes}
    #{'C': None, 'B': None, 'A': None}
    visted = {}
    current = start
    current_dis = 0
    unvisted[current] = current_dis
    while len(unvisted) > 0 or target in unvisted:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisted:
                continue
            new_dist = current_dis + distance
            if unvisted[neighbour] == None or unvisted[neighbour] > new_dist:
                unvisted[neighbour] = new_dist
        visted[current] = current_dis
        print('Appending visited', current, visted[current])
        del unvisted[current]
        if not unvisted or not target in unvisted:
            break
        rest_of_them = [node for node in unvisted.items() if node[1]]
        current, current_dis = sorted(rest_of_them, key=lambda x: x[1])[0]
    print(visted)

dj_shortest(nodes, distances, 'A', 'Z')
