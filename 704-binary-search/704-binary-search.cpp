class Solution {
public:
    int search(vector<int>& nums, int target) {
        int hi = nums.size();
        int lo = 0;
        
        if (hi == 1 && nums[0] == target) { // 1 element edge case
            return 0;
        }
        
        while (lo < hi) {
            int idx = lo + (hi - lo) / 2; // calculate midpoint
            if (nums[idx] == target) {
                return idx;
            }
            else if (nums[idx] < target) { // too low -> move low threshold up
                lo = idx + 1;
            }
            else { // too high
                hi = idx;
            }
        }
        
        return -1;
    }
};