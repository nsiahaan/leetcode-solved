class Solution:
    def rob(self, nums: List[int]) -> int:
        # must rob every other house, use dp approach
        if len(nums) < 3:
            return max(nums)
        
        dp = [nums[0], nums[1]]
        for i in range(2, len(nums), 1):
            dp.append(nums[i] + max(dp[:-1]))
            
        return max(dp[-1], dp[-2])