#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''

def min_coins(coin_list, change):
    if change in coin_list:
        return 1 # 1 coin
    current_min = change
    for coin in coin_list:
        if coin < change:
            numCoin = 1 + min_coins(coin_list, change - coin)
            if numCoin < current_min:
                current_min = numCoin
    return numCoin

def min_coins(coin_list, change):
    attemp = 0
    while attemp

print(min_coins([1,5,10,20,25], 50))
