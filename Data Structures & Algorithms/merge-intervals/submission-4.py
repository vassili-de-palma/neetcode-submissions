class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        s = intervals[0][0]
        e = intervals[0][1]
        ans = []
        for iv in intervals:
            if iv[0] <= e:
                s, e = min(s, iv[0]), max(e, iv[1])
            else:
                ans.append([s,e])
                s, e = iv
        ans.append([s,e])
        return ans



