#!/usr/bin/env python3

'''
DFS of a dictionary tree assignment, CIS 210 

Author: Zhipeng Xie

Credits: 'python.org' official document

Implement of DFS on a dictionary tree
'''

tree1 = {0: [1, 2],
         1: [5, 6],
         2: [3, 4, 7],
         3: [],
         4: [],
         5: [7],
         6: [7],
         7: []
         }

tree2 = {0: [1, 2],
         1: [3, 4],
         2: [5, 6],
         3: [7, 8],
         4: [9, 10],
         5: [],
         6: [],
         7: [],
         8: [],
         9: [],
         10: [],
         11: [],
         12: [],
         13: [],
         14: []
         }


def dfs_path(tmp_dict, start, target, visted=[]):
    '''
    (dict, int, anything, opt list) -> list

    effect: Call the _dfs_path() func to return the path 
    of Depth-first travling of inputed dictionary, check
    if target is in the dictionary or not.

    Input: tmp_dict is a tree represented by dictionary,
    start and target are specified vertices, visted list
    is used to note down the vertices function has been to.

    Output: A list of vertices function has been to, if target
    not founded, return an empty list.

    >>> print(print(dfs_path(tree1, 2 , 7))
    [2, 3, 4, 7]
    >>> print(dfs_path(tree2, 0, 14))
    []
    '''
    path = _dfs_path(tmp_dict, start, target, visted)
    if target not in path:
        return []
    else:
        return path


def _dfs_path(tmp_dict, start, target, visted=[]):
    '''
    (dict, int, anything, opt list) -> list

    Effect:To return the path of Depth-first travling of inputed 
    dictionary.

    Input: tmp_dict is a tree represented by dictionary,
    start and target are specified vertices, visted list
    is used to note down the vertices function has been to.

    Output: A list of vertices function has been to.

    >>> print(print(dfs_path(tree1, 2 , 7))
    [2, 3, 4, 7]
    >>> print(print(dfs_path(tree2, 2 , 6))
    [2, 3, 4, 7, 2, 5, 6]
    '''
    visted.append(start)
    for item in tmp_dict[start]:
        if target in visted:
            break
        _dfs_path(tmp_dict, item, target, visted)
    return visted


def dfs_find(tmp_dict, start, target):
    '''
    (dict, int, anything) -> Boolean

    Effect: Call the _dfs_find() func to determine whether
    a object is in the dictionary or not

    Input: tmp_dict is a tree represented by dictionary, 
    start and target are specified vertices

    Output: The bool result of whether the target is in
    the dictionary tree

    >>> print(dfs_find(tree1, 0, 7))
    True
    >>> print(dfs_find(tree2, 0, 0))
    True
    >>> print(dfs_find(tree2, 0, 14))
    False
    '''
    marker = []
    _dfs_find(tmp_dict, start, target, marker)
    return start == target or True in marker


def _dfs_find(tmp_dict, start, target, marker):
    '''
    (dict, int, anything) -> Boolean or None

    Effect: To determine whether a object is in the 
    dictionary or not(except the start vertex)

    Input: tmp_dict is a tree represented by dictionary, 
    start and target are specified vertices

    Output: The bool result of whether the target is in
    the dictionary tree

    >>> print(dfs_find(tree1, 0, 4))
    True
    >>> print(dfs_find(tree2, 0, 10))
    True
    '''
    if start == target:
        marker.append(True)
    for item in tmp_dict[start]:
        _dfs_find(tmp_dict, item, target, marker)
    return None

print(dfs_path(tree1, 2, 7))
print(dfs_find(tree1, 0, 4))

print(dfs_path(tree2, 2, 6))
print(dfs_find(tree2, 0, 14))


# Real binary-tree & DFS
# I'm really uncomfortable with the dictionary tree
# As a result, I append the real tree version
# Just to prove that I can do it
print('************* Real Binary-tree *****************')

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

    def dfs(self, target):
        visited, stack = [], [self.root]
        while stack:
            node = stack.pop()
            if node.value == target:
                return True
            visited.append(node)
            stack.extend(filter(None, [node.right, node.left]))
        return False

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

example = tree([1, 2, 3, 4])
print(example)
print(example.dfs(3))
print(example.dfs(5))
