#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''

import csv
import re


data_dict = {}
FILE_name = '1488495277.csv'

rule = r'.*(fire|police|steal|leak|gas|emergency|first aid|food|water).*'

the_rule = re.compile(rule)

fire_rule = re.compile(r'.*(fire|leak|gas).*')

police_rule = re.compile(r'.*(police|steal).*')

amblance_rule = re.compile(r'.*(emergency|first aid).*')

resource_rule = re.compile(r'.*(food|water|resource).*')
with open(FILE_name, newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    data_list = list(reader)
    count = 0
    for row in data_list:
        tmp_dict = {}
        tmp_dict['Boolean'] = 0
        tmp_dict['Fire'] = 0
        tmp_dict['Police'] = 0
        tmp_dict['Resource'] = 0
        tmp_dict['Amblance'] = 0
        if fire_rule.match(row['content']):
            tmp_dict['Fire'] = 100
        if police_rule.match(row['content']):
            tmp_dict['Police'] = 100
        if amblance_rule.match(row['content']):
            tmp_dict['Amblance'] = 100
        if resource_rule.match(row['content']):
            tmp_dict['Resource'] = 100
        if the_rule.match(row['content']):
            tmp_dict['Boolean'] = 100
        for title in row:
           if title == 'latitude' or title == 'longitude' or title == 'content' or title == 'title':
                tmp_dict[title] = row[title]
        print(tmp_dict)
        data_dict[count] = tmp_dict
        count += 1    


headers = ['title', 'Boolean', 'latitude', 'longitude', 'content', 'Fire', 'Police', 'Amblance', 'Resource']


with open('result.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    for row in data_dict:
        f_csv.writerow(data_dict[row])
    print('done')


