class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        removed = 0
        curr_start, curr_end = intervals[0]
        for start, end in intervals[1:]:
            if start < curr_end:
                removed += 1
                curr_start = min(curr_start, start)
                curr_end = min(curr_end, end)
            else:
                curr_start, curr_end = start, end
        return removed

            