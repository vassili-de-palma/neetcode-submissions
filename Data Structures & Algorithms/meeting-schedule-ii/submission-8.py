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
        h = []
        rooms = defaultdict(tuple)
        ans = 1

        for i in intervals:
            if not h:
                h.append(i.end)
            else:
                first_end = h[0]
                if i.start >= first_end:
                    heapq.heapreplace(h, i.end)
                else:
                    heapq.heappush(h, i.end)
                    ans += 1
        
        return len(h) 





        
        