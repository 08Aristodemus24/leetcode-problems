from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge cases: [1], [1, 2]
        # start left pointer at 0
        # start right pointer at 1

        left, right = [0, 1]
        n = len(prices)

        # init max profit to 0
        curr_max_profit = 0

        # if n is <= 1 then loop doesn't run anyway and curr_max_profit 0 is returned
        # loop left pointer until n - 2, but what if 2 elem only in prices then n - 2 will be 0
        print(prices)
        print(n - 2)

        # because right pointer will eventually be much faster
        # than left pointer when right is at last element or n-1
        # make last calcs then loop will reach stop condition
        while right <= n - 1:
            profit = prices[right] - prices[left]

            # check if day ahead of current day has greater price and if yes then
            # also check if the profit of these days are greater than current max profit
            if prices[right] > prices[left] and profit > curr_max_profit:
                curr_max_profit = profit
                # right += 1
            elif prices[right] < prices[left]:
                left = right
                # right += 1
            right += 1

        return curr_max_profit
            