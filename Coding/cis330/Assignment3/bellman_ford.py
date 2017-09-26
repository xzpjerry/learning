#!/usr/bin/env python3

graph = {
    'vertices': ['s', 't', 'a', 'b', 'c', 'd', 'e', 'f'],
    'edges': {
        's': [(1, 'a'), (1, 'b'), (1, 'c')],
        'a': [(1, 'd'), (-2, 'e')],
        'b': [(60, 'e')],
        'c': [(65, 'f')],
        'd': [(100, 't')],
        'e': [(70, 't'), (70, 'f')],
        'f': [(-5, 't')],
        't': []
    }
}


def bf(graph, start='s'):

    dis_dict = {vertex: None for vertex in graph['vertices']}

    dis_dict[start] = 0
    has_changed = True
    while has_changed:
        has_changed = False

        for current in graph['edges']:
            print(current)
            for wei, vt in graph['edges'][current]:
                if dis_dict[current] != None:

                    if dis_dict[vt] == None:
                        dis_dict[vt] = dis_dict[current] + wei

                    else:
                        if dis_dict[vt] > dis_dict[current] + wei:

                            dis_dict[vt] = dis_dict[current] + wei
                            has_changed = True

        print(dis_dict)

bf(graph)


#!/usr/bin/env python3

import time


graph = {
    'vertices': ['s', 'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 't'],
    'edges': {
        's': [(1, 'a1'), (50, 'b1')],
        'a1': [(1, 's'), (3, 'a2'), (10, 'b1')],
        'b1': [(50, 's'), (20, 'b2'), (10, 'a1')],
        'a2': [(3, 'a1'), (20, 'a3'), (10, 'b2')],
        'b2': [(20, 'b1'), (2, 'b3'), (10, 'a2')],
        'a3': [(20, 'a2'), (30, 't'), (10, 'b3')],
        'b3': [(2, 'b2'), (4, 't'), (10, 'a3')],
        't': [(30, 'a3'), (4, 'b3')]
    }
}


def min_cost(graph):
    current_min_dict = {vertex: None for vertex in graph['vertices']}
    current_min_dict['s'] = 0

    num_vertices = len(graph['vertices'])

    for i in range(num_vertices - 1):

        for vertex in graph['edges']:

            for wei, vt in graph['edges'][vertex]:

                if current_min_dict[vt] == None:
                    current_min_dict[vt] = current_min_dict[vertex] + wei
                else:
                    current_min_dict[vt] = min(
                        current_min_dict[vt], current_min_dict[vertex] + wei)

    return current_min_dict

start = time.time()
print(min_cost(graph))
end = time.time()
print('BF Way in %.7f' % ((end - start) * 1000)) 