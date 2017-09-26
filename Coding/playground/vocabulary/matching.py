#!/usr/bin/env/python3
import handle_srt
import re
import os.path
import json


def matching(target, fname = None):
    result = ''
    if not os.path.isfile('db.json'):
         with open('db.json', 'w') as tmp:
            json.dump({}, tmp)
    with open('db.json', 'r') as f:
        db = json.loads(f.read())
        if db:
            if fname and fname not in db:
                handle_srt.handler(fname)

            target_cap = target.capitalize()
            target_low = target.lower()
            rule = re.compile(r'.*[\W](%s)([\W].*|$)' %
                              (target + '|' + target_cap + '|' + target_low))

            last_line = None

            for source in db:
                for line in db[source]:
                    for ele in db[source][line]:
                        if rule.match(ele):
                            if int(line) - 1 > 0:
                                result += 'From %s\n' % source
                                result += str([db[source][str(int(line) - 1)]])
                                result += '\n'
                            result += str(db[source][line])
                            result += '\n\n'
                            break
            if result == '':
                result = 'Not found'
        else:
            result = 'Haven\'t import vocalbulary data!'
    return result
