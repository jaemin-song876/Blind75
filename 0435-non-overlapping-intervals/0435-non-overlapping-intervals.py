class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[1])
        count =0
        prev_end = intervals[0][1]

        for interval in intervals[1:]:
            start, end = interval[0], interval[1]

            if start<prev_end:
                count += 1
            else:
                prev_end = end
        return count