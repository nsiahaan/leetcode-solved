class Solution {
public:
    int tribonacci(int n) {
        if (n < 2) {
            return n;
        }
        
        size_t dp[n + 1]; // initialize dp array
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 1;
        
        for (int i = 3; i < n + 1; i++) {
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
        }
        
        return dp[n];
    }
};