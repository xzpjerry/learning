# !/usr/bin/env python3

graph = {
    'vertices': ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'edges': {
        'm': ['q', 'r', 'x', ],
        'n': ['o', 'q', 'u', ],
        'o': ['r', 's', 'v', ],
        'p': ['o', 's', 'z'],
        'q': ['t'],
        'r': ['u', 'y'],
        's': ['r'],
        't': [],
        'u': ['t'],
        'v': ['x', 'w'],
        'w': ['z'],
        'x': [],
        'y': ['v'],
        'z': []
    }
}


class dfs_result(object):

    def __init__(self):
        self.edges_class = {}
        self.order = []
        self.timing = {}
        self.topological_order = []

    def __str__(self):
        result = 'The order of dfs: '
        result += str(self.order)
        result += '\n\nTiming info of each vertex: '
        result += str(self.timing)
        result += '\n\nClassification of each edge: '
        result += str(self.edges_class)
        result += '\n\nTop_order: '
        self.topological_order.reverse()
        result += str(self.topological_order)
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
    noter.topological_order.append((start, total_start_time))
    noter.timing[start][1] = total_start_time


total_start_time = 0

noter = dfs_result()
dfs2dict(graph['edges'], 'm', noter)

print(noter)
