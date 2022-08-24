class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        left, right = 0, len(strx)-1
        
        while left < right:
            if strx[left] != strx[right]:
                return False
            left += 1
            right -= 1
        return True