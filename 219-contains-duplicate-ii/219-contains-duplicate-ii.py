class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set() # maintain a window of recently seen k items
        for i, num in enumerate(nums): # index, number
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k]) # remove the i-kth item -> k=2, {1,2,3} -> {2,3}
        return False