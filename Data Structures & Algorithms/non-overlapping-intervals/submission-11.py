class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        removed = 0
        _, curr_end = intervals[0]
        for start, end in intervals[1:]:
            if start < curr_end:
                removed += 1
                # keep the interval that ends before
                curr_end = min(curr_end, end)
            else:
                curr_end = end
        return removed

            