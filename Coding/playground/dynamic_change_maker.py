import time

coins = [1, 5, 10, 25, 50]

def _get_change(coins, amount, last_coin, result):
    if amount >= last_coin:
        result[last_coin] += 1
        _get_change(coins, amount - last_coin, last_coin, result)
    elif coins:
        current_max_coin = coins.pop()
        _get_change(coins, amount, current_max_coin, result)
    else:
        return



def get_change(coins, amount):
    start_time = time.time()

    coins = sorted(coins)
    result = {coin:0 for coin in coins}
    max_coin = coins.pop()
    _get_change(coins, amount, max_coin, result)

    end_time = time.time()
    print('Time usage: %.5f' % (end_time - start_time))
    return result




def _dy_get_change(table, amount):
    pass


def dy_get_change(coins, amount):
    a_hash_table = {coin:{i:None for i in range(amount + 1)} for coin in coins}
    
    for i in range(amount + 1):
        for coin in coins:
            if coin > i:
                continue

    return result


print(get_change(coins, 97))