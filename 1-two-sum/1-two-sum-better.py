class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # maintain dict of seen values, number:index
        
        for i in range(len(nums)): # O(n)
            subtarget = target - nums[i]
            if subtarget not in seen: # O(1) lookup
                seen[nums[i]] = i
            else:
                if seen[subtarget] != i: # check different indexes
                    return [seen[subtarget], i]
