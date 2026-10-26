class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parents = list(range(n))
        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        count = n
        for u,v in edges:
            ru, rv = find(u), find(v)
            if ru != rv: 
                parents[ru] = rv
                count -= 1

        return count
        