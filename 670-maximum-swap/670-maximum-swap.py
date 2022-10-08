class Solution:
    def maximumSwap(self, num: int) -> int:
        # prioritize bigger numbers at the beginning
        nums = [i for i in str(num)]
        nums.sort(reverse=True) # sort nums in desc. order (priority)
        strnum = str(num)
        newnum = ""
        max_idx = len(strnum) - 1
        swap = 0
        
        for i in range(len(nums)):
            if strnum[i] == nums[i]:
                newnum += nums[i]
            else:
                newnum += nums[i]
                swap = strnum[i] # keep track of the lower number
                for j in range(len(nums) - 1, i, -1): # find index of the rightmost nums[i] in original number
                    if strnum[j] == nums[i]:
                        max_idx = j
                        break
                newnum += strnum[i+1:max_idx] # add numbers between swapped numbers
                newnum += swap # add swapped number
                break
                
        if len(newnum) != len(strnum): # if trailing numbers
            newnum += strnum[max_idx+1:]
        
        return newnum