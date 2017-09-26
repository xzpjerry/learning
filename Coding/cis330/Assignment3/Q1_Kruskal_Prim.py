graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (2, 'A', 'B'), (3, 'A', 'C'), (3, 'A', 'D'),
        (4, 'B', 'E'),
        (4, 'C', 'B'), (5, 'C', 'D'), (1, 'C', 'E'),
        (7, 'D', 'F'),
        (8, 'E', 'F'),
        (9, 'F', 'G')
    ]
}
def union(edge, result, rank):
    def find(v):
        if rank[v] != v:
            rank[v] = find(rank[v])
        return rank[v]

    root_1 = find(edge[1])
    root_2 = find(edge[2])
    if root_1 != root_2:
        result.append(edge)
        rank[edge[2]] = root_1
        return True
    return False

def kruskal(graph):
    result = []
    rank = {}
    visted = []
    edges = sorted([edge for edge in graph['edges']], reverse=True)
    num_component = 0
    for vertex in graph['vertices']:
        rank[vertex] = vertex
        num_component += 1

    while edges and num_component > 1:
        current_edge = edges.pop()
        weight, v1, v2 = current_edge
        if union(current_edge, result, rank):
            num_component -= 1

    print(result)

kruskal(graph)




graph2 = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': {
        'A': [(2, 'B'), (3, 'D'), (3, 'C')],
        'B': [(3, 'E')],
        'C': [(1, 'E'), (4, 'B'), (5, 'D')],
        'D': [(7, 'F')],
        'E': [(8, 'F')],
        'F': [(9, 'G')],
        'G': []
    }
}

def Prim(graph, start='A'):
    MST = []
    unvisited = []

    for vertex in graph['vertices']:
        unvisited.append(vertex)

    current = start
    known_edges = []
    
    while unvisited:

        for wei, vt in graph['edges'][current]:
            edge = (wei, current, vt)
            known_edges.append(edge)

        unvisited.remove(current)

        known_edges.sort(reverse=True)
        while known_edges:
            possible_choice = known_edges.pop()
            wei, v0, vt = possible_choice
            if vt in unvisited:
                MST.append((wei, v0, vt))
                current = vt
                break

    print(MST)



Prim(graph2)
