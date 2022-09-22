class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort() # sort the numbers in increasing order
        n = len(nums)
        
        for i in range(n):
            if i != nums[i]:
                return i
        return len(nums) # if missing number is last number