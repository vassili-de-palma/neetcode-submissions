class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True 

        adj = defaultdict(list)
        indeg = defaultdict(int)
        for a,b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
            indeg[b] += 0

        # starting nodes with no dependencies
        q = deque(node for node in indeg.keys() if indeg[node] == 0)
        order = []

        while q:
            b = q.popleft()
            order.append(b)
            for a in adj[b]:
                indeg[a] -= 1
                if indeg[a] == 0: 
                    q.append(a)
        
        print(order)
        return len(order) == len(indeg)


        