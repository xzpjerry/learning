#!/usr/bin/env python3

'''
An example showing how the 
module works.
Simply put the mother module
in the same path as the caller.
'''

import Memorable_pin
import log_and_sorted
import inherit_test

'''
pin
'''
test = Memorable_pin.Memorable_pin()
test.set_num_Pin(3464140)

'''
sorted
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key = log_and_sorted.by_name))
print(sorted(L, key = log_and_sorted.by_socre, reverse = True))

'''
inherit
'''
a = inherit_test.cat()    