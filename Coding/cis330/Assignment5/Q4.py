import time

coins = [1, 3, 7, 10]

c_dict = {coin:[1, [coin]] for coin in coins}
c_dict[0] = [0, []]

def DP(T):
    if c_dict.get(T):
        return c_dict[T]

    if T < 0:
        return 1000
    global coins
    min_coin_num = 1000
    using_coins = []
    for coin in coins:
        if coin <= T:
            if DP(T - coin)[0] < min_coin_num:
                        min_coin_num = DP(T - coin)[0]
                        using_coins = DP(T - coin)[1] + [coin]
    c_dict[T] = [min_coin_num + 1, using_coins]

    return c_dict[T]

def DPI(T):
    if c_dict.get(T):
        return c_dict[T]

    if T < 0:
        return None

    global coins
    for i in range(1, T + 1):
        if not c_dict.get(i):
            min_coin_num = 1000
            using_coins = []
            for coin in coins:
                if coin <= i:
                    if c_dict[i - coin][0] < min_coin_num:
                        min_coin_num = c_dict[i - coin][0]
                        using_coins = c_dict[i - coin][1] + [coin]
            c_dict[i] = [min_coin_num + 1, using_coins]

    return c_dict[T]

start = time.time()
result = DPI(12)
end = time.time()
print(result, 'In %.7fs' % (end - start))