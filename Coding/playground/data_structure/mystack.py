#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''
import random
class Stack:

    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        result = None
        try:
            result = self.data.pop()
        except:
            pass
        finally:
            return result

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)

def test1():

    def check_parentheses(astr):
        astack = Stack()
        for char in astr:
            if char == '(':
                astack.push(char)
            elif char == ')':
                if astack.pop() == None:
                    astack.push('Shit')
                    break
        return astack

    parentheses = ['()))(()()(()', '((((((())', '()))','(()()()())', '(((())))', '()()()()']


    for acase in parentheses:
        print(acase, 'is ')
        if not check_parentheses(acase).isEmpty():
            print('Not balanced')
        else:
            print('balanced')

def test2():

    def baseConverter(source_num, base):
        rem_stack = Stack()
        num_table = '0123456789ABCDEFGHIJKLMN'
        while source_num > 0:
            rem = source_num % base
            rem_stack.push(rem)
            source_num = source_num // base

        result = ''
        while not rem_stack.isEmpty():
            result += num_table[rem_stack.pop()]

        return result

    print(baseConverter(25,2))
    print(baseConverter(25,16))
    print(baseConverter(25,8))
    print(baseConverter(256,16))
    print(baseConverter(26,26))

if __name__ == '__main__':
    test2()