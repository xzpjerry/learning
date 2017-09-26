#!/usr/bin/env python3
class qNs(object):
    """
    My implement of queue & stack
    """
    class node(object):
        def __init__(self, value):
            self.value = value
            self.front = None
            self.back = None

    def __init__(self):
        self.root = self.node(None)
        self.rightest = self.root
        self.thesize = 0

    def isEmpty(self):
        return self.root.front == None

    def push(self, item, **kw):
        if 'right' in kw and kw['right'] == True:
            tmp_node = self.node(item)
            tmp_node.back = self.rightest
            self.rightest.front = tmp_node
            self.rightest = tmp_node
        else:
            tmp_node = self.node(item)
            tmp_node.back = self.root
            if not self.isEmpty():
                self.root.front.back = tmp_node
            else:
                self.rightest = tmp_node
            tmp_node.front = self.root.front
            self.root.front = tmp_node
        self.thesize += 1

    def pop(self, **kw):
        result = None
        if 'left' in kw and kw['left'] == True:
            if not self.isEmpty():
                tmp = self.root.front
                result = tmp.value
                self.root.front = tmp.front
                self.root.front.back = self.root
                del tmp
                self.thesize -= 1
        else:
            if not self.isEmpty():
                result = self.rightest.value
                self.rightest = self.rightest.back
                del self.rightest.front
                self.rightest.front = None
                self.thesize -= 1
        return result

    def size(self):
        return self.thesize

    def find(self, target):
        if not self.isEmpty():
            current = self.root
            while (current.front):
                current = current.front
                if current.value == target:
                    return True
        return False

    def __str__(self):
        result = 'Root'
        if not self.isEmpty():
            current = self.root
            while (current.front):
                current = current.front
                result += ' <-> %s' % current.value
        return result


M = [
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0]
]

def check(M, src):
    '''
    (list[][] -> list)

    Using bfs to scan the matrix, and note each
    vertex's in and out degree
    '''
    num_vertices = len(M)
    Q = qNs()
    degree_dict = {i:[0,0] for i in range(num_vertices)}
    # [outdegree, indegree]

    start_point = src
    Q.push(start_point)
    while not Q.isEmpty():
        current = Q.pop()
        counter = 0
        for neighbor in M[current]:
            if neighbor == 1:
                degree_dict[current][0] += 1
                degree_dict[counter][1] += 1
                Q.push(counter)
            counter += 1
        if Q.isEmpty() and start_point < num_vertices - 1:
            start_point += 1
            Q.push(start_point)

    result = []

    for vertex in degree_dict:
        if degree_dict[vertex][0] == 0 and degree_dict[vertex][1] == num_vertices - 1:
            result.append(vertex)

    return result

print(check(M, 0))