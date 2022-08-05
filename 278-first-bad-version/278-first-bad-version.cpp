// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        // use 2 ptrs in binary search
        int lo = 1;
        int hi = n;
        int first_bad = n;
        
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (isBadVersion(mid)) {
                if (mid < first_bad) {
                    first_bad = mid;
                }
                hi = mid;
            }
            else {
                lo = mid + 1;
            }
        }
        
        return first_bad;
    }
};