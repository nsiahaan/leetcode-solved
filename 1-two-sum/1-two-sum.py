class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos1 = 0
        pos2 = 1
        
        found = False
        for i in range(len(nums)):
            if found:
                break
            if nums[i] > target and target > 0:
                continue
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    pos1 = i
                    pos2 = j
                    found = True
                    break
        return [pos1, pos2]
        