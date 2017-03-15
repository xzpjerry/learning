#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''

import os
import re

dirtory = input('Folder_path:')
rule = re.compile(r'.*.(py)$')
all_the_file = [f for f in os.listdir(dirtory) if os.path.isfile(os.path.join(dirtory, f)) and rule.match(f)]

print(all_the_file)
'''
with open(result, 'r') as f:
    result = f.readlines()
    print(result)
'''