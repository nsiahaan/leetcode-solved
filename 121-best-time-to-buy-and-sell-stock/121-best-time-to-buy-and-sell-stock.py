class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        target = prices[-1] # start at end of list
        for i in range(len(prices) - 1, -1, -1):
            # for each item in the list, compare with target and record profit. update target to greatest #
            if prices[i] > target: 
                target = prices[i]
            else:
                if (target - prices[i]) > profit:
                    profit = target - prices[i]
        return profit