#!/usr/bin/env python3
'''
    Intro to Data_analysis

    Author: Zhipeng Xie

    Credits: 'python.org' official document,
    "Programming In Context" page 170

    Input a list of data(number), to do some data
    analysis job(mean, median, mode, frequency table/chart)
'''
import turtle


sample_data = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3,
               2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6,
               4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1,
               4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9,
               2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7,
               4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7,
               3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1,
               2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1,
               2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3,
               6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
               2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
               2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9,
               4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5,
               4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6,
               2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1,
               2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1,
               2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5,
               4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1,
               4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0,
               2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
               3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5,
               2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
               2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7,
               2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6,
               2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9,
               2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1,
               3.1, 4.6, 2.8, 3.1, 6.3]

class database(object):

    def __init__(self, alist):
        '''
        (list) -> None

        Effect: Initial variables, using the inputed
        list. Call mean(), median(), mode(), frequencyTable(),
        frequencyChart() funcs to do data analysis job

        Input: List needed to be handled

        Output: Nothing returned

        >>> example = database(sample_data)
            print(example)
        !!'List a frequency table'!! omitted
        'Pop out python turtle, making a chart about the data'
        omitted
        'mean: 3.780749
        median: 3.300000
        mode_list: [2.5]'

        >>> example = database([1,2,3,4])
            print(example)
        ITEM FREQUENCY
        1         1
        2         1
        3         1
        4         1
        'Pop out python turtle, making a chart about the data'
        omitted
        mean: 2.500000
        median: 2.500000
        mode_list: [1, 2, 3, 4]

        '''
        self.original_data = sorted(alist)
        self.len_of_data = len(self.original_data)
        self.modelist = []
        self.item_list = []
        self.count_dict = {}
        self.mean = None
        self.max_count = None
        self.median = None
        '''
        self._mean()
        self._median()
        self._mode()
        self._frequencyTable()
        #self._frequencyChart()
        '''

    def _mean(self):
        '''
        (none) -> none

        Effect: To calculate the mean value of inputed
        list

        No input needed

        No output

        Example is in the __init__ func
        '''
        self.mean = sum(self.original_data) / self.len_of_data

    def _median(self):
        '''
        (none) -> none

        Effect: To calculate the median value of inputed value

        No input needed

        No output

        Example is in the __init__ func
        '''
        is_even = (self.len_of_data % 2 == 0)
        if is_even:
            right_mid = self.len_of_data // 2
            left_mid = right_mid - 1
            self.median = (self.original_data[
                           left_mid] + self.original_data[right_mid]) / 2
        else:
            mid = self.len_of_data // 2
            self.median = self.original_data[mid]

    def _mode(self):
        '''
        (none) -> none

        Effect: To find the number that appears the most times

        No input needed

        No output

        Example is in the __init__ func
        '''
        for item in self.original_data:
            if item in self.count_dict:
                self.count_dict[item] = self.count_dict[item] + 1
            else:
                self.count_dict[item] = 1

        countlist = self.count_dict.values()
        self.max_count = max(countlist)

        for item in self.count_dict:
            if self.count_dict[item] == self.max_count:
                self.modelist.append(item)

    def _frequencyTable(self):
        '''
        (none) -> none

        Effect: To list how many times each element has
        appeared in the inputed list

        No input needed

        No output

        Example is in the __init__ func
        '''
        self.item_list = list(self.count_dict.keys())
        self.item_list.sort()
        print('ITEM FREQUENCY')
        for item in self.item_list:
            print(item, '       ', self.count_dict[item])

    def _frequencyChart(self):
        '''
        (none) -> none

        Effect: Using turtle's functions to draw a chart to
        represent how many times each element has appeared 
        in the inputed list

        No input needed

        No output

        Example is in the __init__ func
        '''
        max_item = len(self.item_list) - 1
        win = turtle.Screen()
        chartT = turtle.Turtle()
        win.setworldcoordinates(-1, -1, max_item + 1, self.max_count)
        chartT.hideturtle()

        chartT.up()
        chartT.goto(0, 0)
        chartT.down()
        chartT.goto(max_item, 0)
        chartT.up()

        chartT.goto(-1, 0)
        chartT.write('0')
        chartT.goto(-1, self.max_count)
        chartT.write(str(self.max_count))

        for index in range(len(self.item_list)):
            chartT.goto(index, -1)
            chartT.write(str(self.item_list[index]))

            chartT.goto(index, 0)
            chartT.down()
            chartT.goto(index, self.count_dict[self.item_list[index]])
            chartT.up()
        win.exitonclick()

    def __str__(self):
        '''
        (none) -> Strng

        Effect: To make a formated printing

        No input needed

        Output: A formated String of mean, median, mode_list value

        Example is in the __init__ func
        '''
        result = ''
        result += 'mean: %f' % self.mean
        result += '\nmedian: %f' % self.median
        result += '\nmode_list: %s' % self.modelist
        return result

if __name__ == '__main__':
    example = database(sample_data)
    example._frequencyChart()
    print(example)

    #another_example = database([1,2,3,4])
    #print(another_example)
