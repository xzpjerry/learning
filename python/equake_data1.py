#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''
import urllib.request
from data_analysis import database
import re


def readeqi():
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
    whole_analysis = database(mag_list)
    whole_analysis._mean()
    whole_analysis._median()
    whole_analysis._mode()
    results = (whole_analysis.mean, whole_analysis.median,
               whole_analysis.modelist, whole_analysis)
    return results


def equake_report(mag_list, mmm_tuple, need_chart):
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
    mag_list = readeqi()
    mmm_tuple = equake_analysis(mag_list)
    equake_report(mag_list, mmm_tuple, True)

equake_main()
