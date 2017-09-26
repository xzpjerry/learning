#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''

class bin_tree(object):
    class node(object):
        def __init__(self, value = None):
            self.value = value
            self.lchild = None
            self.rchild = None

    def __init__(self):
        self.root = node()

    def _find_the_right_place(self, current_node, target):
        if target < current_node.value:
            if current_node.lchild
            _find_the_right_place(self.lchild, target)

    def add_num(self, item):
        if self.root.lchild != None:
            x = node(item)
        else:
            self.root.lchild = node(item)
            self.root.value = True