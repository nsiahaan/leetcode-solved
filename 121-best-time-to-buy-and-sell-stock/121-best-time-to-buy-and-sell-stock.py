class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = set()
        target = prices[-1] # start at end of list
        for i in range(len(prices) - 1, -1, -1):
            # for each item in the list, compare with target and record profit. update target to greatest #
            if prices[i] > target: 
                target = prices[i]
            else:
                profits.add(target - prices[i])
        return max(profits)