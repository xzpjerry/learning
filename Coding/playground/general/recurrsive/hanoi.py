#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''

def moveDisk(source, sink):
    print('Moving from %s to %s' % (source, sink))

def moveTower(height, source, sink, tmp_tower):
    if height >= 1:
        moveTower(height - 1, source, tmp_tower, sink)
        moveDisk(source, sink)
        moveTower(height - 1, tmp_tower, sink, source)

moveTower(3, 'A', 'B', 'C')
