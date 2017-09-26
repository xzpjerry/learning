#!/usr/bin/env python3

graph = {
    'vertices': [0, 1, 2, 3, 4, 5],
    'edges': {
        # vertex:{another_vertex: weight/distance, ... },
        0: {1: 1},
        1: {2: 1},
        2: {3: 1},
        3: {4: 1},
        4: {5: 1},
        5: {}
    }
}
top_oder = [0, 1, 2, 3, 4, 5]
'''
When topological order is the same as vertices order,
the graph should looks like the following:
0 -> 1 -> 2 -> 3 -> 4 -> 5
'''


def get_longest_path(graph, top_oder):
    '''
    (dict, []) -> int

    Returning the longest distance between the vertex has
    least topological order and the one has the most top
    order 
    '''
    stack = []
    for vertex in top_oder:
        stack.append(vertex)
    try:
        target = stack.pop()
    except:
        target = None

    current_longest = 0
    while stack:
        origin = stack.pop()
        if target in graph['edges'][origin]:
            # If origin -> target, means connected
            current_longest += graph['edges'][origin][target]
        target = origin

    return current_longest


print(get_longest_path(graph, top_oder))
