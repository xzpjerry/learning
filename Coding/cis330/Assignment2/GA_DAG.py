#!/usr/bin/env python3


class graph(object):

    def __init__(self, gn):
        '''
        To initial the adjacency data structure
        '''
        self.graph_num = gn
        self.num_nodes = int(input())
        self.num_edges = int(input())
        self.nodes = [i for i in range(self.num_nodes)]
        self.edges = {i + 1: [] for i in range(self.num_nodes)}

        for i in range(self.num_edges):

            raw_edge = input().split()
            self.edges[int(raw_edge[0])].append(int(raw_edge[1]))

    def __str__(self):
        result = 'Graph number: %s' % str(self.graph_num + 1)
        result += '\nTop order: %s' % str(self.top_order)
        result += '\nLongest: %s' % str(self.longest_path)
        result += '\nShrotest: %s' % str(self.shortest2n)
        result += '\nPaths: %s\n' % str(self.num_paths)
        return result

    def get_top_order(self):
        self.top_order = []
        self._dfs()

    def _dfs(self):
        stack = []
        stack.append(1)
        while stack:
            current = stack.pop()
            if current not in self.top_order:
                self.top_order.append(current)
                for neighbour in reversed(self.edges[current]):
                    if neighbour not in self.top_order:
                        stack.append(neighbour)

    def DAG_job(self):
        Num_path_dict = {i + 1: 0 for i in range(self.num_nodes)}
        Num_path_dict[1] = 1
        shortest_dis = {i + 1: None for i in range(self.num_nodes)}
        shortest_dis[1] = 0
        longest_dis = {i + 1: 0 for i in range(self.num_nodes)}

        for i in self.top_order:

            for connected in self.edges[i]:

                Num_path_dict[connected] += Num_path_dict[i]

                if shortest_dis[connected] == None or shortest_dis[connected] > shortest_dis[i] + 1:
                    shortest_dis[connected] = shortest_dis[i] + 1

                if longest_dis[connected] < longest_dis[i] + 1:
                    longest_dis[connected] = longest_dis[i] + 1

        self.num_paths = Num_path_dict[self.num_nodes]
        self.longest_path = longest_dis[self.num_nodes]
        self.shortest2n = shortest_dis[self.num_nodes]

num_graphs = int(input())

for i in range(num_graphs):
    a_graph = graph(i)
    a_graph.get_top_order()
    a_graph.DAG_job()
    print(a_graph)
