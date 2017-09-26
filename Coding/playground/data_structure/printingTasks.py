#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''
from myqueue import myqueue
import random
from multiprocessing.dummy import Pool as threadPool

class Task(object):

    def __init__(self, time):
        self.pages = random.randrange(1, 21)
        self.startTime = time

    def getPages(self):
        return self.pages

    def waitTime(self, FinishedTime):
        return FinishedTime - self.startTime


class Printer(object):

    def __init__(self, PagesPerMin):
        self.ppm = PagesPerMin
        self.currentTask = None
        self.timeRemainingInSec = 0

    def New_task(self, task):
        self.currentTask = task
        self.timeRemainingInSec = task.getPages() * 60 / self.ppm

    def is_busy(self):
        return self.currentTask != None

    def timeFlying(self):
        if self.currentTask != None:
            self.timeRemainingInSec -= 1
            if self.timeRemainingInSec == 0:
                self.currentTask = None


def main(args):
    TotalSeconds, PPM = args
    Aprinter = Printer(PPM)
    printQueue = myqueue()
    waitTimes = []

    def new_task_coming():
        tmp = random.randrange(0, 91)
        if tmp == 90:
            return True
        return False

    for aSec in range(TotalSeconds):

        if new_task_coming():
            task = Task(aSec)
            printQueue.push(task)

        if not Aprinter.is_busy():
            if not printQueue.isEmpty():
                nextTask = printQueue.pop()
                waitTimes.append(nextTask.waitTime(aSec))
                Aprinter.New_task(nextTask)

        Aprinter.timeFlying()

    avg_wait_time = sum(waitTimes) / len(waitTimes)
    return 'Average wait %.2f sec(s), %d tasks remaining' % (avg_wait_time, printQueue.size())

repeat_times = 10 

result_10 = []
args_10_ppm = [(3600, 10) for i in range(repeat_times)]

result_5 = []
args_5_ppm = [(3600, 5) for i in range(repeat_times)]

p1 = threadPool(2)
result_10 = p1.map(main, args_10_ppm)
p1.close()
p1.join()

p2 = threadPool(2)
result_5 = p2.map(main, args_5_ppm)
p2.close()
p2.join()

for index in range(repeat_times):
    print('Using 5PPM:', result_5[index])
    print('Using 10PPM:', result_10[index], '\n')
