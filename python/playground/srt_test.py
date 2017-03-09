#!/usr/bin/env/python3
import re
from collections import OrderedDict
import json
tmp_line_num = 0
with open('the.srt', 'r') as f:
    handled_dict = OrderedDict()
    for line in f.readlines():
        line = line.strip()
        if re.match(r'.*-->.*', line):
            tmp_line_num += 1
            handled_dict[tmp_line_num] = []
        if tmp_line_num and re.match(r'.*[:|a-zA-Z].*', line):
            handled_dict[tmp_line_num].append(line)
    if handled_dict != {}:
        with open('handled_srt.json', 'w') as tmp_json:
            json.dump(handled_dict, tmp_json)


with open('handled_srt.json', 'r') as f:
    db = json.loads(f.read())
    target = input('What are you looking for?:')
    target_cap = target.capitalize()
    target_low = target.lower()
    rule = re.compile(r'.*[\W](%s)([\W].*)|$' % (target + '|' + target_cap + '|' + target_low))
    result = []
    for key in db:
        for ele in db[key]:
            if rule.match(ele):
                result.append(key)
                break

    for key in result:
        print(db[key])

    if not result:
        print('Not found')
