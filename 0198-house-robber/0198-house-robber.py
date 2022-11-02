class Solution:
    def rob(self, nums: List[int]):
        '''
        if len(nums) <= 2:
            return max(nums)
        else:
            return max(nums[0]+self.rob(nums[2:]), self.rob(nums[1:]))
        
        '''
        # must rob any non-adjacent house, use dp approach
        if len(nums) < 3:
            return max(nums)
        
        dp = [nums[0], max(nums[0],nums[1])]
        for i in range(2, len(nums)):
            #dp.append(nums[i] + max(dp[:-1]))
            dp.append(max(dp[i-1], nums[i] + dp[i-2]))
            
        return max(dp[-1], dp[-2])
        