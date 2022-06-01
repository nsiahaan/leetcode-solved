from math import ceil
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        # print(length)
        nums = []
        p1, p2 = 0, 0
        
        while len(nums) <= length//2:
            if p1 == len(nums1): # case: uneven arrays, but sorted array not built
                nums.append(nums2[p2])
                p2 += 1
                continue
            elif p2 == len(nums2):
                nums.append(nums1[p1])
                p1 += 1
                continue
                
            if nums1[p1] < nums2[p2]:
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1
        
        print(nums, length, length%2)
        if length % 2 == 0: # even number of elements
            med = (nums[-1] + nums[-2]) / 2.0
            return med
        else:
            return nums[-1]
        