#!/usr/bin/env python3


graph = {
    'vertices': ['s', 't', 'a', 'b', 'c', 'd', 'e', 'f'],
    'edges': {
        's': [(0.8, 'a'), (0.5, 'b'), (0.4, 'c')],
        'a': [(0.1, 'd'), (1, 'e')],
        'b': [(0.6, 'e')],
        'c': [(0.4, 'f')],
        'd': [(0.1, 't')],
        'e': [(0.2, 't'), (0.9, 'f')],
        'f': [(0.8, 't')],
        't': []
    }
}


def mod_dj(graph, start, end):

    visted = []
    max_band_dict = {vertex: None for vertex in graph['vertices']}
    known_edges = []

    current = start
    max_band_dict[current] = 1

    while len(visted) < len(graph['vertices']):

        print(current)

        if current not in visted:
            visted.append(current)

        for edge in graph['edges'][current]:

            wei, neighbour = edge

            if neighbour not in visted:
                known_edges.append(edge)

            if max_band_dict[neighbour] == None:
                max_band_dict[neighbour] = wei * max_band_dict[current]
            else:
                max_band_dict[neighbour] = max(
                    max_band_dict[neighbour], max_band_dict[current] * wei)

        known_edges.sort()

        while known_edges:

            possible_next = known_edges.pop()
            wei, vt = possible_next

            if vt not in visted:
                current = vt
                break

    print(max_band_dict)

mod_dj(graph, 's', 't')
