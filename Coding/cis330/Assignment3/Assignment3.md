Name: Zhipeng Xie

UO ID: 951586566


# Q1 Kruskal & Prim


## Using Kruskal
### The graph object structure is like the following:

```Graph = {	‘nodes’=  [a, b ,c ,…, l]	‘edges’= [ (9, ‘a’,’b’), …, (weight,  v1, v2)]	}

Example:
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
```

### Defining the Union function:

```
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
```
* Edge structure: (weight, v0, vt)
* Result is the MST result, represnting in dictionary structure.
* Rank list is used to determine whether adding this edge would cause a cycle or not.

#### Main algorithm
```
def kruskal(graph):
    result = []
    rank = {}
    visted = []
    edges = sorted([edge for edge in graph['edges']], reverse=True)
    # edges list would be used as a stack
    # now the top of it is the edge with smallest weight
    
    for vertex in graph['vertices']:
        rank[vertex] = vertex

    while edges:
        current_edge = edges.pop()
        weight, v1, v2 = current_edge
        has_v1 = v1 in visted
        has_v2 = v2 in visted
        
        if not has_v1 or not has_v2: 
            #So, we must encouter a new vertex
            
            new = v2 if has_v1 else v1
            visted.append(new)
            union(current_edge, result, rank)
           
    print(result)
```

## Using Prim
### The graph data structure is like the following:
```
graph = {
    'vertices': [v1, v2, ... , vn],
    'edges': {
        v1: [(w1, vi), (w2, vj) ,..., (wm, vk)],
        v2: [......],
        ...
        vn: [(weight, vt)]
    }
}

Example:
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
```
### Main algorithm
```
def Prim(graph, start='A'):
    MST = []
    unvisited = [vertex for vertex in graph['vertices']]

    current = start
    known_edges = []
    
    while unvisited:

        # To grab new encountered edges
        for wei, vt in graph['edges'][current]:
            edge = (wei, current, vt)
            known_edges.append(edge)
            Previous_node[vt] = current
		
        unvisited.remove(current)
        known_edges.sort(reverse=True)
        
        while known_edges:
        
        	# So the top of known_edges is the shortest 
            possible_choice = known_edges.pop()
            
            wei, v0, vt = possible_choice
            if vt in unvisited:
                MST.append((wei, v0, vt))
                current = vt
                break

    print(MST)
```

***

# Q2 Modified Dijkstra
> Finding number of shortest path

## The graph data structure is like the following:
```
graph = {
    'vertices': [v1, v2, ... , vn],
    'edges': {
        v1: [(w1, vi), (w2, vj) ,..., (wm, vk)],
        v2: [......],
        ...
        vn: [(weight, vt)]
    }
}

Example:
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
```

## Main Algorithm
```
def Mod_dj(graph, start='A'):
	'''
	E.g output: {'A': 1, 'B': 1, 'E': 1, 'F': 1, 'I': 2, 'J': 2} 
	{'A': 0, 'B': 7, 'E': 8, 'F': 3, 'I': 17, 'J': 13}
	
	First one is a dictionary representing the Number of shortest path from start to each vertex,
	second one shows the shortest weight from start to each vertex.
	'''
    visted = []
    MST = {vertex: None for vertex in graph['vertices']}
    Num_path_dict = {vertex: 0 for vertex in graph['vertices']}
    tracker = []
    
    current = start
    has_repeated = False

    MST[current] = 0
    Num_path_dict[current] = 1

    while len(visted) < len(graph['vertices']):

        possible_next = None
        if current not in visted:
            visted.append(current)

        for weight, neighour in graph['edges'][current]:
            if neighour not in visted:

                if possible_next == None or weight < possible_next[0]:
                    possible_next = (weight, neighour)

                if MST[neighour] == None or MST[neighour] > MST[current] + weight:
                    
                    # So, This is the first time we encounter this vertex
                    # Or, we find a shorter path
                    MST[neighour] = MST[current] + weight
                    Num_path_dict[neighour] = 1

                elif MST[neighour] == MST[current] + weight and not has_repeated:
                	
                	# Found another path's weight is equal to known_shortest path 
                    Num_path_dict[neighour] += 1

        try:
            next_start = possible_next[1]
            has_repeated = False
            
        except:
        	# So current vertex hasn't connected to any unknown vertex
        	# We have to go back to previous vertex
            next_start = tracker.pop()
            has_repeated = True

        tracker.append(current)
        current = next_start

	print(Num_path_dict, MST)
```

***

# Q3 Modified Dijkstra
> Output the bandwidth of a path with max bandwidth from s to t

Slightly modify the Dijkstra algorithm can reach the goal.

## The graph data structure is like the following:
```
graph = {
    'vertices': [v1, v2, ... , vn],
    'edges': {
        v1: [(w1, vi), (w2, vj) ,..., (wm, vk)],
        v2: [......],
        ...
        vn: [(weight, vt)]
    }
}

Example:
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
```

## Main Algorithm
```
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
                
                		# Max_band to vt depens on minimal band between current vertex's maximal band and the weight
                    max_band_dict[vt] = min(max_band_dict[current], weight)
                    
                else:
                
                		# If we found another path result in greater bandwidth, then take it.
                    max_band_dict[vt] = max(max_band_dict[vt], min(max_band_dict[current], weight))
                    
            else:
            
            		# Max bandwidth of vertices connected to the start node are the weithts of edges connected to them.
                max_band_dict[vt] = weight

        known_edges.sort()
        
        while known_edges:
        
        		# So the top of the stack is the edge with greatest bandwidth so far.
            possible_next = known_edges.pop()
            weight, vt = possible_next
            if vt not in visted:
                current = vt
                break
        print(max_band_dict)
```

***

# Q4
> Output the most best reliability weight from start node to each other vertex

Slightly modify the Dijkstra algorithm can reach the goal.

## The graph data structure is like the following:
```
graph = {
    'vertices': [v1, v2, ... , vn],
    'edges': {
        v1: [(w1, vi), (w2, vj) ,..., (wm, vk)],
        v2: [......],
        ...
        vn: [(weight, vt)]
    }
}

Example:
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
```
## Main Algorithm

```
def mod_dj(graph, start, end):
	'''
	Sample output:{'s': 1, 't': 0.5760000000000001, 'a': 0.8, 'b': 0.5, 'c': 0.4, 'd': 0.08000000000000002, 'e': 0.8, 'f': 0.7200000000000001}
	'''

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
```

***

# Q5

## A
> '(M(i,j)^2 == 1 imply?'

There's at least a path from i to j.

> '(M(i,j)^2 == 0 imply?'

There's no path from i to j.

## B
> '(M(i,j)^2 == k imply?'

The shortest path, from i to j, weights k.

***

# Q6

So, node 'm' is one step from the terminating node(Vt) on the shortest path.

Although we don't know how many iterations does it take finally get here,

we know that after this iteration, nothing would change.

## The graph data structure is like the following:
```
graph = {
    'vertices': [v1, v2, ... , vn],
    'edges': {
        v1: [(w1, vi), (w2, vj) ,..., (wm, vk)],
        v2: [......],
        ...
        vn: [(weight, vt)]
    }
}

Example:
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
```

## Main Algorithm
```
def bf(graph, start='s'):
	'''
	Sample output:
	
	After 2 iteration, stop at the 3rd iteration.
	
	{'s': 0, 't': 61, 'a': 1, 'b': 1, 'c': 1, 'd': 2, 'e': -1, 'f': 66}
	
	Shortest path from s to t is: S -> C -> F -> T
	'''
	
    dis_dict = {vertex: None for vertex in graph['vertices']}

    dis_dict[start] = 0
    has_changed = True
    
    while has_changed:
        has_changed = False
		
		# To examinate each edge
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
```