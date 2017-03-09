#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic: Project 8 Part 1/1

Effect: To analyze a file of the majors 
of students in CIS 210 in Winter 2017.

Credits: Python official document
'''
from collections import Counter
import re


class majorData(object):

    def __init__(self):
        '''
        none -> none

        Auto call the majors_main() to do the main jobs

        >>> example = majorData()
        Most frequently occurring major: CIS

        Major    FREQUENCY
        CIS      69
        UNDL     12
        MATH     11
        PBA      7
        MACS     7
        PHYS     7
        PSY      5
        MUP      2
        EC       2
        BI       2
        PREB     2
        ACTG     1
        ART      1
        J        1
        BIC      1
        PJ       1
        GS       1
        HIST     1
        PHIL     1
        CH       1
        PEN      1
        '''
        self.handled_list = []
        self.majors_main()

    def readmajorsf(self, fname):
        '''
        (String) -> list

        Function readmajorsf will have one parameter, fname, a string,
        which is the name of the majors file. readmajorsf should open file
        fname and create and return a list of the majors in this file.
        It's using regular expression to eliminate unnecessary infos,
        in order to get the major informations

        >>> print(readmajorsf('majors_cis210w17.txt'))
        ['CIS', 'CIS', 'MACS', 'MACS', 'MACS', 'CIS', 'CIS', 'CIS', 'PHYS', 'GS', 
        'MATH', 'CIS', 'CIS', 'PBA', 'UNDL', 'CIS', 'CIS', 'PHYS', 'MUP', 'CIS', 'CIS',
         'CIS', 'PBA', 'UNDL', 'CIS', 'UNDL', 'PBA', 'CIS', 'MATH', 'CIS', 'CIS', 'CIS', 
         'CIS', 'PBA', 'UNDL', 'PJ', 'CIS', 'CIS', 'MATH', 'CIS', 'CIS', 'CIS', 'CIS', 
         'CIS', 'PHYS', 'CIS', 'PSY', 'PHYS', 'PBA', 'PEN', 'J', 'CIS', 'BI', 'CIS', 'CIS',
          'PSY', 'CIS', 'PSY', 'CIS', 'CIS', 'CIS', 'ART', 'UNDL', 'CIS', 'UNDL', 'CIS', 'UNDL', 
          'EC', 'CIS', 'CIS', 'HIST', 'PHYS', 'UNDL', 'MATH', 'CIS', 'CIS', 'PREB', 'MACS', 'CIS', 
          'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'PHYS', 'BI', 'CIS', 'EC', 'CIS', 'UNDL', 'CH', 'PBA', 
          'PHYS', 'PSY', 'PSY', 'PBA', 'CIS', 'MUP', 'MACS', 'CIS', 'CIS', 'CIS', 'CIS', 'CIS', 'UNDL', 
          'MATH', 'MATH', 'ACTG', 'MATH', 'CIS', 'CIS', 'PHIL', 'MACS', 'CIS', 'CIS', 'CIS', 'MATH', 'CIS',
           'CIS', 'PREB', 'BIC', 'MATH', 'CIS', 'UNDL', 'CIS', 'MACS', 'CIS', 'CIS', 'CIS', 'MATH', 'UNDL', 
           'CIS', 'CIS', 'CIS', 'MATH', 'CIS']
        '''
        rule = re.compile(
            r'([a-zA-Z\/]+)\s(?P<major>[a-zA-Z]+)\s(\r\n|\r|\n){0,1}')
        self.handled_list = []
        with open(fname, 'r') as content:
            for line in content.readlines():
                tmp_line = rule.match(line)
                if tmp_line:
                    self.handled_list.append(tmp_line.group('major'))
        return self.handled_list

    def report(self, majorsli):
        '''
        (list) -> none

        Function report will have one parameter, majorsli, and return the None value.
        It will call function mode to determine the most frequently occurring item (major)
        in the argument list, and then report the result. report will also call frequencyTable
        to report the number of occurrences for each item in majorsli.

        >>> self.report(readmajorsf('majors_cis210w17.txt'))
        Most frequently occurring major: CIS

        Major    FREQUENCY
        CIS      69
        UNDL     12
        MATH     11
        PBA      7
        MACS     7
        PHYS     7
        PSY      5
        PREB     2
        BI       2
        EC       2
        MUP      2
        BIC      1
        ACTG     1
        ART      1
        HIST     1
        J        1
        PJ       1
        CH       1
        PEN      1
        PHIL     1
        GS       1
        '''
        self._mode()
        self._frequencyTable()
        return None

    def _mode(self):
        '''
        none -> none

        Using a counter to count the list, generating a dict, then sort it into a list in
        descent order, get the first one and it's the most frequency occurring one

        >>> self._mode()
        Most frequently occurring major: CIS 
        '''
        self.raw_counter = Counter()
        for major in self.handled_list:
            self.raw_counter[major] += 1
        self.count_list = sorted(
            self.raw_counter.items(), key=lambda x: x[1], reverse=True)
        self.mode = self.count_list[0]
        print('Most frequently occurring major:', self.mode[0])
        return None

    def _frequencyTable(self):
        '''
        (none) -> none

        Effect: To list how many times each element has
        appeared in the inputed list

        No input needed

        No output

        Example is in the __init__ func
        '''
        print('\nMajor    FREQUENCY')
        for attr in self.count_list:
            print('%-8s %d' % (attr[0], attr[1]))
        return None

    def majors_main(self):
        '''
        none -> none

        majors_main has no parameters and will return the None value.
        It will open a file containing a list of college and major codes,
        which will be in arbitrary order. Each line of the file will have
        a college and major code and every line in the file except for the
        first line, the header ("Major"), contains a college and major code
        (there are no blank lines).

        Example is in the __init__ func
        '''
        # fname = 'majors_short.txt'
        fname = 'majors_cis210w17.txt'
        majorsli = self.readmajorsf(fname)
        self.report(majorsli)
        return None

if __name__ == '__main__':
    Example = majorData()
