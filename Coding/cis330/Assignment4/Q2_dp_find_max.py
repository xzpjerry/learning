#!/usr/bin/env python3

Graph = {
    'vertices': ['s', 'a', 'b', 'c', 'd', 'v'],
    'edges': {
        's': [(7, 'a')],
        'a': [(7, 's'), (15, 'b')],
        'b': [(15, 'a'), (50, 'v'), (100, 'c')],
        'c': [(100, 'b'), (1000, 'd')],
        'd': [(1000, 'c')],
        'v': [(50, 'b')]
    }
}


Max_dict = {vertex: None for vertex in Graph['vertices']}
Max_dict['s'] = 0
visted = []


def M(v):
    '''

    {'s': 0, 'a': None, 'b': None, 'c': None, 'd': None, 'v': None}
    {'s': 0, 'a': 7, 'b': None, 'c': None, 'd': None, 'v': None}
    {'s': 0, 'a': 7, 'b': 15, 'c': None, 'd': 1000, 'v': None}
    {'s': 0, 'a': 7, 'b': 15, 'c': 1000, 'd': 1000, 'v': None}
    {'s': 0, 'a': 7, 'b': 1000, 'c': 1000, 'd': 1000, 'v': None}
    {'s': 0, 'a': 7, 'b': 1000, 'c': 1000, 'd': 1000, 'v': 1000}
    '''
    visted.append(v)

    if Max_dict[v] == None:
        temp_max_wei = -1
        for wei, u in Graph['edges'][v]:
            if temp_max_wei < wei:
                temp_max_wei = wei
            if u not in visted:
                Max_dict[v] = max(M(u), wei)

        if Max_dict[v] == None:
            Max_dict[v] = temp_max_wei

    print(Max_dict)

    return Max_dict[v]
