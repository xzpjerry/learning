#!/usr/bin/env python3
import re

def brain(num1, num2):
    print(num1 + num2, num1 * num2)

if __name__ == '__main__':
    try:
        times = int(input('Input how many test case(s):').strip())
    except:
        times = 0
    finally:
        for i in range(times):
            try:
            	raw = input('Input 2 numbers, using space to separate them:')
            	raw = re.split(r'[\s]', raw)
            	num1 = int(raw[0])
            	num2 = int(raw[1])
            except:
            	num1 = 0
            	num2 = 0
            finally:
            	brain(num1, num2)