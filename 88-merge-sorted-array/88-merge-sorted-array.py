class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = []
        
        p1, p2 = 0, 0
        while p1 != m and p2 != n:
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        
        while p1 != m: # uneven lists
            merged.append(nums1[p1])
            p1 += 1
            
        while p2 != n:  
            merged.append(nums2[p2])
            p2 += 1
            
        for i in range(len(merged)): # replace the values in nums1
            nums1[i] = merged[i]