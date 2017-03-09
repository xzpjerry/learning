#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''
graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'edges': set([
            (1, 'A', 'E'),
            (3, 'A', 'B'),
            (4, 'B', 'E'),
            (5, 'B', 'C'),
            (6, 'E', 'C'),
            (7, 'E', 'D'),
            (2, 'C', 'D'),
            ])
        }

class kruskal(object):

    def __init__(self, graph):
        self.parent = {}
        self.rank = {}
        for vertex in graph['vertices']:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0
            # at first, every vertex is an individual, the same rank, is its parent

        self.get_the_minimal_tree(graph)
        print(self.minimal_tree)

    def find(self, vertex):
        if self.parent[vertex] != vertex: # if not, it means it has been annexed by others
            self.parent[vertex] = self.find(self.parent[vertex]) # to find the one who first annexed others
        return self.parent[vertex]

    def union(self,v1, v2): # to merge without making cycles
        root1 = self.find(v1)
        root2 = self.find(v2) # now we get two identical vertices in two (un)connected part
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]: 
                    self.rank[root1] += 1

    def get_the_minimal_tree(self, graph):
        self.minimal_tree = set()

        edge_counter = 0
        edges = list(graph['edges'])
        edges.sort(key=lambda x: x[0])
        for edge in edges:
            weight, v0, vt = edge
            if self.find(v0) != self.find(vt): # not the same part, won't make a cycle
                print('Merging %s andin %s' %(v0, vt))
                print(self.find(v0), self.find(vt))
                Not_at_the_same_part = True
                self.union(v0, vt)
                Mearge_these_two_part = True
                self.minimal_tree.add(edge)

example = kruskal(graph)