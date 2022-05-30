class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        strnums = [str(x) for x in nums] # convert nums to strings, O(n)
        strnums.sort(cmp=lambda x, y: cmp(x+y, y+x), reverse = True) # sort by first digit in the number, desc., O(nlogn)
        #print('sorted', strnums)
        final = ""
        
        for i in strnums:
            final += i  
        final = final.lstrip('0') # remove leading 0s
        if final == "": # in the event all 0s get removed
            final = "0"
            
        return final
                
            