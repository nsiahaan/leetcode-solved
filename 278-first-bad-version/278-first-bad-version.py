# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # use binary search
        first_bad = n
        
        lo, hi = 1, n
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if (isBadVersion(mid)):
                if mid < first_bad:
                    first_bad = mid # update first bad
                hi = mid # move threshold down
            else: # midpoint is OK
                lo = mid + 1
        return first_bad

        