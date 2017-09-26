#!/usr/bin/env python3
class qNs(object):
    """docstring for queue"""
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
    [0,0,0,1,1],
    [0,0,0,1,1],
    [0,0,0,1,1],
    [1,1,1,0,0],
    [1,1,1,0,0]
    ]

def check(M, src):
    n = len(M)
    vertex_dict = {i:-1 for i in range(n)}
    vertex_dict[src] = 1
    # 1 = 'Good guy'; 0 = 'Bad guy'
    Q = qNs()
    Q.push(src)
    while not Q.isEmpty():
        current = Q.pop()
        counter = 0
        for connection in M[current]:
            if connection and vertex_dict[counter] == -1:
                vertex_dict[counter] = 1 - vertex_dict[current]
                Q.push(counter)
            elif connection and vertex_dict[counter] == vertex_dict[current]:
                return False
            counter += 1
    return True

print(check(M, 0))
