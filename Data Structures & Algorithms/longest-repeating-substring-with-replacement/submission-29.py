class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        lo = 0
        hi = 1
        frq = defaultdict(int)
        ans = 0
        while hi > lo and hi <= n:
            frq[s[hi-1]] += 1
            if max(frq.values()) >= hi - lo - k:
                ans = max(ans, hi - lo)
                hi += 1 
            else:
                frq[s[lo]] -= 1
                frq[s[hi-1]] -= 1
                lo += 1
        return ans

