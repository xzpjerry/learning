#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''

graph = {
        'vertices': ['A', 'B', 'C', 'D', 'Z'],
        'edges': set([
            (2, 'A', 'C'),
            (3, 'A', 'B'),
            (4, 'D', 'Z'),
            (6, 'D', 'C'),
            (8, 'B', 'Z'),
            (2, 'B', 'D')
            ])
        }

class prim(object):

    def __init__(self, graph, start):
        self.edges = sorted(graph['edges'], key = lambda x: x[0])
        self.visted = []
        self.unvisted = []
        self.parent = {}
        self.rank = {}
        for vertex in graph['vertices']:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0
            self.unvisted.append(vertex)

        self.optimal_tree = []
        self.unvisted.remove(start)
        self.visted.append(start)
        self.prim_main()
        print(self.optimal_tree)

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2

    def prim_main(self):
        while len(self.unvisted) > 0:
            for edge in self.edges:
                weight, v0 ,v1 = edge
                has_v0 = v0 in self.visted
                has_v1 = v1 in self.visted
                if has_v0 != has_v1:
                    if self.find(v0) != self.find(v1):
                        if has_v0:
                            self.visted.append(v1)
                            self.unvisted.remove(v1)
                            self.union(v0,v1)
                            self.optimal_tree.append(edge)
                        else:
                            self.visted.append(v0)
                            self.unvisted.remove(v0)
                            self.union(v0,v1)
                            self.optimal_tree.append(edge)
                        self.edges.remove(edge)
                        break

example = prim(graph, 'A')