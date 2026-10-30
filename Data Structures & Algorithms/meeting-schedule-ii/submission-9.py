"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        
        intervals.sort(key=lambda x: x.start)
        ends = []

        for iv in intervals:
            if ends and iv.start >= ends[0]:
                heapq.heapreplace(ends, iv.end)
            else:
                heapq.heappush(ends, iv.end)

        return len(ends) 





        
        