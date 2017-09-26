#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic: Equake_data analysis 1

Effect: Analysis data from a http link

'''
import urllib.request
from data_analysis import database
import re


def readeqi():
    '''
    none -> list

    effect: to read a url from usgs, and filter the magnitude info

    no input

    output: a list of magnitude numbers

    >>> readeqi()
    [5.2, 5.1, 6.0, 5.9, 5.9, 6.0, 5.6, 5.6, 5.7, 5.0, 5.0, 5.2, 5.1, 5.4, 5.2, 5.6]
    '''
    url = 'http://earthquake.usgs.gov/fdsnws/event/1/\
    query?format=csv\
    &starttime=1916-02-01\
    &latitude=44.0519\
    &longitude=-123.0867\
    &maxradiuskm=250\
    &minmagnitude=5'
    mag_list = []
    with urllib.request.urlopen(url) as data:
        the_rule = re.compile(r'.*,(-12\d.*?),(-?\d.*?),(?P<mag>\d.*?),.*')
        for line in data.readlines():
            if the_rule.match(str(line)):
                mag_list.append(the_rule.match(str(line)).group('mag'))
    mag_list = [float(x) for x in mag_list]
    return mag_list


def equake_analysis(mag_list):
    '''
    (list) -> tuple

    effect: Using the previous project's class to analysis the magnitude
    number list

    input: magnitude info list

    output: a tuple of mean, median, modelist value and also my raw
    analysis class instance
    '''
    whole_analysis = database(mag_list)
    whole_analysis._mean()
    whole_analysis._median()
    whole_analysis._mode()
    results = (whole_analysis.mean, whole_analysis.median,
               whole_analysis.modelist, whole_analysis)
    return results


def equake_report(mag_list, mmm_tuple, need_chart):
    '''
    (list, tuple, bool) -> none

    effect: integrate all the analysis infomations into a string,
    and if we need a analysis chart, using previous project's function
    to draw it

    input: magnitude list, tuple from the result equake_analysis, boolean
    of whether we need a chart

    output: none

    >>> mag_list = readeqi()
        mmm_tuple = equake_analysis(mag_list)
        equake_report(mag_list, mmm_tuple, True)
    ITEM FREQUENCY
    5.0         2
    5.1         2
    5.2         3
    5.4         1
    5.6         3
    5.7         1
    5.9         2
    6.0         2
    mean: 5.468750
    median: 5.500000
    mode_list: [5.6, 5.2]
    (Draw a chart)
    '''
    result = ''
    result += 'mean: %f' % mmm_tuple[0]
    result += '\nmedian: %f' % mmm_tuple[1]
    result += '\nmode_list: %s' % mmm_tuple[2]
    tmp_database = mmm_tuple[3]
    tmp_database._frequencyTable()
    if need_chart:
        tmp_database._frequencyChart()
    print(result)
    return None


def equake_main():
    '''
    none -> none

    effect: main function, calling functions above

    no input, output

    >>> equake_main()
    ITEM FREQUENCY
    5.0         2
    5.1         2
    5.2         3
    5.4         1
    5.6         3
    5.7         1
    5.9         2
    6.0         2
    mean: 5.468750
    median: 5.500000
    mode_list: [5.6, 5.2]
    (Draw a chart)
    '''
    mag_list = readeqi()
    mmm_tuple = equake_analysis(mag_list)
    equake_report(mag_list, mmm_tuple, True)
    return None

equake_main()
