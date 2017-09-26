#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic: Project 9 Part 2

Effect: Implement the K-Means Cluster Analysis Algorithm From 
Ch. 7 of the Text and Use It to Analyze and Graphically Report
Earthquake Data.

'''
import random
import urllib.request
import re
import turtle
import threading
from multiprocessing import cpu_count
from multiprocessing.dummy import Pool as ThreadPool
import itertools
#from multiprocessing import cpu_count


def readeqi():
    '''
    none -> list

    effect: to read a url from usgs, and filter the magnitude info

    no input

    output: a list of magnitude numbers

    >>> readeqi()
    'Too many info to show here'
    '''
    url = 'http://earthquake.usgs.gov/fdsnws/event/1/\
query?format=csv\
&starttime=2016-02-01\
&minmagnitude=5'
    info_list = []
    with urllib.request.urlopen(url) as data:
        the_rule = re.compile(
            r'^(?P<date>.*)T(?P<time>.*:.*:.*?\.\d{3})Z,(?P<latitude>.*?\.\d{4}),(?P<longitude>.*?\.\d{4}),[0-9\.]{,5},(?P<mag>.*?),.*')
        for line in data.readlines():
            if the_rule.match(str(line)):
                tmp_tuple = (the_rule.match(str(line)).group('mag'), float(the_rule.match(str(
                    line)).group('latitude')), float(the_rule.match(str(line)).group('longitude')))
                info_list.append(tmp_tuple)
    data_dict = {x: info_list[x] for x in range(len(info_list))}
    return data_dict


def euclidD(p1, p2):
    '''
    (list, list) -> float

    Effect: To show distance between p1 and p2

    Input: 2 lists which represent 2 points, including cooridnations

    Output: Direct distance between p1 and p2

    >>> euclidD([0,0], [1,1])
    1.4142135623730951
    >>> euclidD([0,0], [2,2])
    2.8284271247461903
    '''
    the_sum = 0
    assert len(p1) == len(p2)
    for index in range(len(p1)):
        if isinstance(p1[index], float):
            tmp = (p1[index] - p2[index]) ** 2
            the_sum += tmp
    return the_sum ** 0.5


def createCentroids(k, data_dict):
    '''
    (int, dict) -> list

    Effect: To randomly chose k numbers center points
    from data_dict

    Input: Number of center points needed, raw data_dict

    Output: A list of K numbers of center points

    >>> createCentroids(2, {0:'a', 1:'b', 2:'c', 3:'d'})
    ['b', 'd']
    >>> createCentroids(3, {0:'a', 1:'b', 2:'c', 3:'d'})
    ['a', b', 'd']
    '''
    center_list = []
    while len(center_list) < k:
        tmp_key = random.randrange(0, len(data_dict))
        if tmp_key not in center_list:
            center_list.append(tmp_key)
    return [data_dict[x] for x in center_list]


def createClusters(num_of_cluster, centroids, data_dict, num_of_debug_repeat):
    '''
    (int, list, dict, int) -> list

    Effect: To create clusters based on the center points we already have. In
    each cluster, every point it has has the shortest distance to its center point.
    Repeat serval times to make sure the clusters are what we want.

    Input: Number of cluster we want(I think this can be omited), a list of center
    points, raw data_dict, number of time we want it to repeat

    Output: A list including number of cluster lists, which include serval points
    that are the closest to a center point

    >>>test_dict = {x - 97:(chr(x), x * 10 ** random.random(), 2 * x) for x in range(97, 107)}
    centroids = createCentroids(3, test_dict)
    clusters = createClusters(3, centroids, test_dict, 1)
    print(clusters)
    [[('d', 232.13340913797765, 200), ('f', 244.24718570306203, 204), ('h', 267.14426737852483, 208)],
     [('c', 187.65689840295389, 198), ('g', 143.1305293888369, 206), ('j', 206.4049943553588, 212)], 
     [('a', 771.7129726790187, 194), ('b', 324.08867563636505, 196), ('e', 650.1860107719965, 202), 
     ('i', 457.2483126180674, 210)]]

    '''
    for time in range(num_of_debug_repeat):
        print('**** It\'s the %d time(s) iteration ' % time)
        clusters = []
        for cluster in range(num_of_cluster):
            clusters.append([])

        for key in data_dict:
            current_min_dis = [(euclidD(data_dict[key], centroids[0]), 0)]
            for cluster_index in range(num_of_cluster):
                tmp_dist = euclidD(data_dict[key], centroids[cluster_index])
                if tmp_dist < current_min_dis[0][0]:
                    current_min_dis.pop()
                    current_min_dis.append((tmp_dist, cluster_index))
            index = current_min_dis[0][1]
            clusters[index].append(data_dict[key])

    return clusters


def visualizeQuakes(k, r):
    '''
    (int, int) -> none

    Effect: Using turtle to point out every point from
    the result of readeqi() func, calling createCentroids 
    and createClusters functions to creat clusters

    Input: k --number of clusters, r --number of repetation for 
    creating clusters

    Output: Nothing return, but will pop out a turtle window
    to point out the dots

    >>> cannot provide example
    '''
    data_dict = readeqi()
    
    '''
    def eqDraw(k, eqDict, eqClusters, atuple):
        x, y, cluster_index, aturtle, colorlist = atuple
        aturtle.speed(0)
        aturtle.hideturtle()
        aturtle.up()
        aturtle.color(colorlist[cluster_index])
        aturtle.setpos(x, y)
        aturtle.dot()
    '''
    centroids = createCentroids(k, data_dict)
    clusters = createClusters(k, centroids, data_dict, r)

    quakeWindow = turtle.Screen()
    quakeWindow.bgpic('worldmap.gif')
    quakeWindow.screensize(1800, 900)

    wFactor = quakeWindow.screensize()[0] / (2 * 180)
    hFactor = quakeWindow.screensize()[1] / (2 * 90)

    colorlist = ['red', 'green', 'blue', 'orange', 'cyan', 'yellow']

    '''
    quakeT = turtle.Turtle()
    for cluster_index in range(k):
        for the_tuple in clusters[cluster_index]:
            lat = the_tuple[1]
            lon = the_tuple[2]
            theargs = (lon * wFactor, lat * hFactor, cluster_index,
                       quakeT, colorlist)
            eqDraw(k, data_dict, clusters, theargs)
    '''

    # using multithreading to point out every point

    class longTimeJob(threading.Thread):
        def __init__(self, data, factors, color):
            threading.Thread.__init__(self)
            self.data = data
            self.factors = factors
            self.color = color

        def turtle_dot(self):
            wFactor, hFactor = self.factors
            sub_turtles = itertools.cycle([turtle.Turtle() for i in range(cpu_count())])

            def dot_job(args):
                x, y, aturtle = args
                print('Thread %s is doing its jobs, color is %s' %
                      (threading.current_thread(), self.color))
                aturtle.speed(0)
                aturtle.hideturtle()
                aturtle.up()
                aturtle.color(self.color)
                aturtle.setpos(x, y)
                aturtle.dot()

            args = []
            for item in self.data:
                lat = item[1]
                lon = item[2]
                arg = (lon * wFactor, lat * hFactor, sub_turtles.__next__())
                # dot_job(arg)
                args.append(arg)

            p = ThreadPool()
            p.map(dot_job, args)
            p.close()

        def run(self):
            print('Im %s' % threading.current_thread())
            self.turtle_dot()

    for i in range(k):
        worker = longTimeJob(clusters[i], (wFactor, hFactor), colorlist[i])
        worker.start()

    quakeWindow.exitonclick()
    return None

if __name__ == '__main__':
    visualizeQuakes(6, 2)
