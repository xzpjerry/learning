#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''


class myqueue(object):
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

def test():
    aqueue = myqueue()
    bools = [True, False]
    for i in range(20):
        to_push = random.randrange(0,2)
        to_pop = random.randrange(0,2)
        to_right = random.randrange(0,2)
        to_left = random.randrange(0,2)
        if bools[to_push]:
            print('Gona push %d' %i)
            if bools[to_right]:
                print('Gona push it to the rightest')
                aqueue.push(i,right=True)
            else:
                print('TO the leftest')
                aqueue.push(i)
        elif bools[to_pop]:
            print('Gona pop')
            if bools[to_left]:
                print('Gonna pop the leftest')
                aqueue.pop(left=True)
            else:
                print('Gonna pop the rightest')
                aqueue.pop()
        print(aqueue)
        print('')

if __name__ == '__main__':
    '''
    To compare time consuming between python's queue and mine,
    when handling 10k individuals get in and get out, repeating 
    10 times

    result:
    Mine:
    34.53962456499994 s

    Pyrhon's:
    71.62528959599967 s
    '''
    import random
    test()
