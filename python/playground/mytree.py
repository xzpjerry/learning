#!/usr/bin/env python3


class Node:
    def __init__(self, value):
        self.leftc = None
        self.rightc = None
        self.value = value


class mytree:
    def __init__(self):
        self._root = None

    @property
    def Root(self):
        return self._root

    @Root.setter
    def Root(self, value):
        self._root = Node(value)

    def add(self, value):
        if isinstance(value, int):
            if(self._root == None):
                self.Root = value
            else:
                self._add(value)
        else:
            pass

    def _add(self, value, node=None):
        if node == None:
            node = self.Root
        if(value < node.value):
            if(node.leftc != None):
                self._add(value, node.leftc)
            else:
                node.leftc = Node(value)
        else:
            if(node.rightc != None):
                self._add(value, node.rightc)
            else:
                node.rightc = Node(value)

    def find(self, target):
        if self.Root != None:
            return self._find(target, self.Root)
        return False

    def _find(self, target, node):
        if target == node.value:
            return True
        elif target > node.value and node.rightc != None:
            return self._find(target, node.rightc)
        elif target < node.value and node.leftc != None:
            return self._find(target, node.leftc)
        else:
            return False

    def _printTree(self, node):
        if node.leftc != None:
            self._printTree(node.leftc)
        print(node.value)
        if node.rightc != None:
            self._printTree(node.rightc)

    def printTree(self):
        if self.Root != None:
            self._printTree(self.Root)
        else:
            print('empty tree')

    def get_the_mid_and_add(self, tmp_list):
        if len(tmp_list) != 0:
            self._get_the_mid_and_add(tmp_list)
        else:
            pass

    def _get_the_mid_and_add(self, tmp_list):
        if len(tmp_list) == 1 and not self.find(tmp_list[0]):
            self.add(tmp_list[0])
        elif len(tmp_list) > 1:
            len_of_list = len(tmp_list)
            mid_pos = len_of_list // 2
            mid = tmp_list[mid_pos]
            self.add(mid)
            self._get_the_mid_and_add(tmp_list[:mid_pos])
            self._get_the_mid_and_add(tmp_list[mid_pos:len_of_list])
        else:
            pass


a = mytree()
arry = []
a.get_the_mid_and_add(arry)
a.printTree()
print(a.find(3))
