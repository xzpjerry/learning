#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''
import turtle
import random
def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-random.randrange(branchLen//2),t)
        t.left(40)
        tree(branchLen-random.randrange(branchLen//2),t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    t.speed(0)
    tree(100,t)
    myWin.exitonclick()

main()