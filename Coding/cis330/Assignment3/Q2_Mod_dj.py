graph = {
    'vertices': ['A', 'B', 'E', 'F', 'I', 'J'],
    'edges': {
        'A': [(9, 'B'), (3, 'F'), (8, 'E')],
        'B': [(9, 'A'), (4, 'F')],
        'E': [(8, 'A'), (6, 'F'), (9, 'I'), (5, 'J')],
        'F': [(3, 'A'), (4, 'B'), (6, 'E'), (10, 'J')],
        'I': [(9, 'E'), (4, 'J')],
        'J': [(5, 'E'), (10, 'F'), (4, 'I')]
    }
}


def dj(graph, start='A', end=None):
    visted = []
    MST = {vertex: None for vertex in graph['vertices']}
    Num_path_dict = {vertex: 0 for vertex in graph['vertices']}
    tracker = []
    current = start
    has_repeated = False

    MST[current] = 0
    Num_path_dict[current] = 1

    while len(visted) < len(graph['vertices']):
        print(current)
        possible_next = None
        if current not in visted:
            visted.append(current)

        for weight, neighour in graph['edges'][current]:
            if neighour not in visted:

                if possible_next == None or weight < possible_next[0]:
                    possible_next = (weight, neighour)

                if MST[neighour] == None or MST[neighour] > MST[current] + weight:
                    MST[neighour] = MST[current] + weight
                    Num_path_dict[neighour] = 1

                elif MST[neighour] == MST[current] + weight and not has_repeated:
                    Num_path_dict[neighour] += 1

        try:
            next_start = possible_next[1]
            has_repeated = False
        except:
            next_start = tracker.pop()
            has_repeated = True

        tracker.append(current)
        current = next_start

    print(Num_path_dict, MST)


dj(graph)
