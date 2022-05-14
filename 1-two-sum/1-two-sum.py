class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        index = 0
        
        for i in nums:
            tgt = target - i
            
            if tgt in d:
                return [index, d[tgt]]
            d[i] = index
            index += 1

        return None # no solution
            