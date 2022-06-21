class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search, two ptrs moving to middle, stop at intersection
        if len(nums) == 1:
            if nums[0] == target:
                return 0
        
        left, right = 0, len(nums)-1 # ptrs, will also be index
        while left < right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[left] < target:
                left += 1
            else:
                right -= 1
        return -1