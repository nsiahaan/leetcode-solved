class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int: 
        d = defaultdict(int)
        count = 0
        
        for num in time:
            # print(num, -num, num%60, -num % 60, d[-num%60])
            count += d[-num % 60] # -num % 60 is the (reduced) complement
            d[num % 60] += 1 # remember reduced form
        return count