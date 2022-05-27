class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0]) # sort by first elem in intervals, ascending
        overlaps = [intervals[0]]
        i = 1
        
        while i < len(intervals):
            if overlaps[-1][1] >= intervals[i][0]:
                overlaps[-1][1] = max(overlaps[-1][1], intervals[i][1])
                i += 1
            else:
                overlaps.append(intervals[i])
                i += 1    
        return overlaps    