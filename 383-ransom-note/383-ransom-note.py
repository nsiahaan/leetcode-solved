class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # for each letter in note, check if exists in magazine
        # if exists, remove letter from magazine
        letters = {}
        for letter in magazine:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        
        for letter in ransomNote:
            if letter in letters:
                if letters[letter] <= 0:
                    return False
                letters[letter] -= 1
            else:
                return False
        return True