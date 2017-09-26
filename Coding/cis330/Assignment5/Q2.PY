

X = [0, 1, 10, 10, 1]
F = [0, 1, 2, 4, 8]

DP_dict = {i: None for i in range(len(X))}
DP_dict[0] = 0
print(DP_dict)


def DP(i):
    if DP_dict[i] != None:
        return DP_dict[i]

    global X
    global F

    DP_dict[i] = max(DP(i - t) + min(X[i], F[t]) for t in range(1, i + 1))

    return DP_dict[i]

print(DP(4))
print(DP_dict)
