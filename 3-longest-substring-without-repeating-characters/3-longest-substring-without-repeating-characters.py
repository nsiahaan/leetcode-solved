class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = set()
        left, right = 0, 0
        
        while right < len(s):
            if s[right] in current:
                if longest < len(current):
                    longest = len(current)
                current.clear()
                left += 1
                right = left
            else:
                current.add(s[right])
                right += 1
            
        if longest < len(current):
            longest = len(current)
        return longest