MT = {
    'a': {'a': 'b', 'b': 'b', 'c': 'a'},
    'b': {'a': 'c', 'b': 'b', 'c': 'a'},
    'c': {'a': 'a', 'b': 'c', 'c': 'c'}
}

DP_table = {(a + b, MT[a][b]): True for a in MT for b in MT[a]}
DP_table2 = {(a, a): True for a in MT}
DP_table = {**DP_table, **DP_table2}

print(DP_table)

S = 'bbbba'


def DP(S, t):
    print(S, t)
    global MT
    if DP_table.get((S, t)):
        return DP_table[(S, t)]

    current = False

    for a in ['a', 'b', 'c']:
        for b in ['a', 'b', 'c']:
            if MT[a][b] == t:
                for k in range(1, len(S)):
                    if not current:
                        current = DP(S[:k], a) and DP(S[k:], b)
                    else:
                        break
    DP_table[(S, t)] = current

    return DP_table[(S, t)]


print(DP(S, 'c'))
print(DP_table)
