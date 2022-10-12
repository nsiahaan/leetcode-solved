class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search -> need midpoint approach
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]: 
                if nums[mid] > nums[mid - 1]: # peak
                    return mid
                else: # reduce search space in half
                    right = mid
            else:
                left = mid + 1
        return left
        
        '''
        # realized this is O(n)
        # use L + R ptrs, for each L/R check if > neighbors -> return L/R else move on
        if len(nums) == 1:
            return 0
        
        left, right = 0, len(nums) - 1
        if nums[left] > nums[left + 1]: # edge peaks, return right away
            return left
        if nums[right] > nums[right - 1]:
            return right
        left += 1
        right -= 1
        
        while left <= right:
            if nums[left - 1] < nums[left] and nums[left] > nums[left + 1]:
                return left
            if nums[right - 1] < nums[right] and nums[right] > nums[right + 1]:
                return right
            else: # no peak
                left += 1
                right -= 1
        '''