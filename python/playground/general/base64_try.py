#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic: base64

Effect: eliminate the '=' symbol of the result
of base64 encodeing

'''

import base64

def safe_base64_decode(s):
    len_s = len(s)
    while len_s % 4 != 0:
        s += b'='
        len_s = len(s)
    return base64.b64decode(s)

print(type(safe_base64_decode(b'abcd')))
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
