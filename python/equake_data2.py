#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''
import unittest
import random

def euclidD(p1, p2):
    the_sum = 0
    assert len(p1) == len(p2)
    for index in range(len(p1)):
        tmp = (p1[index] - p2[index]) ** 2
        the_sum += tmp
    return the_sum ** 0.5


def createCentroids(k, data_dict):
    num_of_done = 0
    center_list = []
    while  num_of_done < k:
        tmp_key = random.randrange(0, len(data_dict))
        if tmp_key not in center_list:
            center_list.append[tmp_key]
    return [data_dict[x] for x in center_list]


def createClusters():
    pass


class test_eqdt(unittest.TestCase):

    def test_euclidD(self):
        self.assertEqual(euclidD((0,0), (1,1)), 2 ** 0.5)

    def test_creatcenter()

unittest.main()