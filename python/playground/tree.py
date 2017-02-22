from queue import Queue


class Node(object):

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class tree(object):

    def __init__(self, alist):
        self.root = None
        self.str_result = ''
        self.original_data = sorted(alist)
        self.visited = []
        self.get_the_mid_and_add(self.original_data)

    def add(self, ele):
        if self.root == None:
            self.root = Node(ele)
        else:
            self._add(self.root, ele)

    def _add(self, node, ele):
        if(ele < node.value):
            if(node.left != None):
                self._add(node.left, ele)
            else:
                node.left = Node(ele)
        else:
            if(node.right != None):
                self._add(node.right, ele)
            else:
                node.right = Node(ele)

    def get_the_mid_and_add(self, tmp_list):
        if len(tmp_list) != 0:
            self._get_the_mid_and_add(tmp_list)
        else:
            pass

    def _get_the_mid_and_add(self, tmp_list):
        if len(tmp_list) == 1 and tmp_list[0] not in self.visited:
            self.add(tmp_list[0])
        elif len(tmp_list) > 1:
            len_of_list = len(tmp_list)
            mid_pos = len_of_list // 2
            mid = tmp_list[mid_pos]
            self.add(mid)
            self.visited.append(mid)
            self._get_the_mid_and_add(tmp_list[:mid_pos])
            self._get_the_mid_and_add(tmp_list[mid_pos:len_of_list])
        else:
            pass

    def _printTree(self, node):
        self.printTree(node.left)
        self.str_result += str(node.value) + ' '
        self.printTree(node.right)

    def printTree(self, node):
        if node != None:
            self._printTree(node)

    def __str__(self):
        self.printTree(self.root)
        return self.str_result
