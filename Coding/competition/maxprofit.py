#!/usr/bin/env python3

prices = [0, 1, 2, 3, 0, 2]
DP_table = {0:0,1:0}

lowest_price = [9999]
count_day = 0
current_low = None
for day in range(1, len(prices)):
    if current_low == None:
        current_low = prices[day]
    elif current_low > prices[day]:
        current_low = prices[day]
    lowest_price.append(current_low)

print(lowest_price)
print(DP_table)

def DP(day):
    global DP_table
    global prices
    global lowest_price
    if day in DP_table:
        return DP_table[day]

    DP_table[day] = max(DP(day - 1), DP(day - 2) + prices[day - 2] - lowest_price[day - 3])

    return DP_table[day]


print(DP(5))
print(DP_table)
