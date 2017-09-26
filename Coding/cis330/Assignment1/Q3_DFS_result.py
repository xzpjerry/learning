#!/usr/bin/env python3


graph = {
    'vertices': ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'edges': {
        'w': ['s'],
        'v': ['w'],
        'x': ['z'],
        'q': ['s', 't', 'w'],
        'z': ['x'],
        'u': ['y'],
        'r': ['u', 'y'],
        's': ['v'],
        't': ['x', 'y'],
        'y': ['q']
    }
}


class dfs_result(object):

    def __init__(self):
        self.edges_class = {}
        self.order = []
        self.timing = {}

    def __str__(self):
        result = 'The order of dfs: '
        result += str(self.order)
        result += '\nTiming info of each vertex: '
        result += str(self.timing)
        result += '\nClassification of each edge: '
        result += str(self.edges_class)
        return result


def dfs2dict(adict, start, noter):
    noter.order.append(start)

    global total_start_time
    total_start_time += 1
    noter.timing[start] = [total_start_time, -1]  # [start_time, end_time]

    for vertex in adict[start]:

        # this vertex is first time encoutered
        if vertex not in noter.order:
            noter.edges_class[(start, vertex)] = 'Tree'
            dfs2dict(adict, vertex, noter)
        else:

            # this vertex hasn't finished yet
            if noter.timing[vertex][1] == -1:
                noter.edges_class[(start, vertex)] = 'Back'

            # this vertex is discovered later than start point
            elif noter.timing[vertex][0] > noter.timing[start][0]:
                noter.edges_class[(start, vertex)] = 'Forward'

            # this vertex is neither start's ancestor nor descendant
            else:
                noter.edges_class[(start, vertex)] = 'Cross'

    total_start_time += 1
    noter.timing[start][1] = total_start_time


total_start_time = 0

noter = dfs_result()
dfs2dict(graph['edges'], 'q', noter)

print(noter)
