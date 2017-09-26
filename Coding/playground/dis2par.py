#!/usr/bin/env python3

astring = 'BOBOBOB'

def dis(i, j):
    global astring
    if i == j:
        return 1
    if j == i - 1:
        return 0

    if astring[i] == astring[j]:
        return dis(i + 1, j - 1) + 2
    else:
        return max(dis(i, j - 1), dis(i + 1, j))

print(dis(0, len(astring) - 1))
