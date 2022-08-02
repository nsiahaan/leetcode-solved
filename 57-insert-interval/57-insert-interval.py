class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:        
        intervals.append(newInterval) # insert into list
        intervals.sort(key = lambda x: x[0]) # sort by first value
        
        # merge overlapping intervals
        i = 0
        final = []
        while i < len(intervals):
            # if overlap
            if final and final[-1][-1] >= intervals[i][0]:
                final[-1][-1] = max(intervals[i][1], final[-1][-1])
            else:
                final.append(intervals[i])
            i += 1
        return final