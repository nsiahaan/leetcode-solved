class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
                
        for char in t:
            if char in letters:
                letters[char] -= 1
                if letters[char] < 0:
                    return False
            else:
                return False
        
        for char in letters:
            if letters[char] > 0:
                return False
            
        return True