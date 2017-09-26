#!/usr/bin/env python3
import time

graph = {
    'vertices': ['s', 't', 'a', 'b', 'c', 'd', 'e', 'f'],
    'edges': {
        's': [(8, 'a'), (5, 'b'), (4, 'c')],
        'a': [(3, 'd'), (3, 'e')],
        'b': [(4, 'e')],
        'c': [(3, 'f')],
        'd': [(1, 't')],
        'e': [(3, 't'), (4, 'f')],
        'f': [(4, 't')],
        't': []
    }
}


def mod_dj(graph, start, end):

    visted = []
    max_band_dict = {vertex: None for vertex in graph['vertices']}
    known_edges = []

    current = start
    max_band_dict[current] = -1
    while end not in visted:
        print(current)
        if current not in visted:
            visted.append(current)

        for edge in graph['edges'][current]:
            known_edges.append(edge)
            weight, vt = edge
            if max_band_dict[current] != -1:
                if max_band_dict[vt] == None:
                    max_band_dict[vt] = min(max_band_dict[current], weight)
                else:
                    max_band_dict[vt] = max(max_band_dict[vt], min(max_band_dict[current], weight))
            else:
                max_band_dict[vt] = weight

        known_edges.sort()
        while known_edges:
            possible_next = known_edges.pop()
            weight, vt = possible_next
            if vt not in visted:
                current = vt
                break
        print(max_band_dict)

mod_dj(graph, 's', 't')
