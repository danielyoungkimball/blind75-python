# Best Time to Buy and Sell Stock - LeetCode 121
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # -> arr[int]
        # return int "profit"

        profit = 0
        min_value = prices[0]

        for i , value in enumerate(prices):
            # set min
            if value < min_value:
                min_value = value
            
            if (value - min_value > profit):
                profit = (value - min_value)

        return profit

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))  # Output: 5
