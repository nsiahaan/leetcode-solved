class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = "" # maintain prefix
        # let the first word set target letter
        # for remaining letters, match same index with target letter, add to pref if valid
        if len(strs) == 1:
            return strs[0]
        strs.sort(key=len)
        
        for i in range(len(strs[0])):
            target = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != target:
                    return prefix
            prefix += target
        return prefix