#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''

import hashlib

db = {
}


def get_md5(password):
    tmp_md5 = hashlib.md5()
    tmp_md5.update((password + ' the-Salt').encode('utf-8'))
    return tmp_md5.hexdigest()

def login(user, password):
    return db[user] == get_md5(password)

def register(username, password):
    db[username] = get_md5(password)

register('michael', '123456')
print(login('michael','123456'))
