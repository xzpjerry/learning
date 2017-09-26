#!/usr/bin/env python3

prices = [1, 2, 3, 0, 2]
#maxProfit = 3
#transactions = [buy, sell, cooldown, buy, sell]


class Solution(object):
    def maxProfit(self, prices):
        '''
        :type prices: List[int]
        :rtype: int
        '''
        num_days = len(prices)

        if num_days < 2:
            return 0

        current_sell_max = 0
        current_buy_cheapest = -prices[0]

        pre_sell = 0
        pre_buy = 0

        for day in range(num_days):
            pre_buy = current_buy_cheapest
            current_buy_cheapest = max(pre_sell - prices[day], current_buy_cheapest)

            pre_sell = current_sell_max
            current_sell_max = max(pre_buy + prices[day], pre_sell)

        return current_sell_max

        

a = Solution()
print(a.maxProfit(prices))
