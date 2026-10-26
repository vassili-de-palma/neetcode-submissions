class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        subgraphs = []
        visited = set()
        while len(visited) != n:
            for i in range(n):
                if i not in visited: 
                    source = i
                    break
            q = deque([source])
            visited.add(source)
            subgraphs.append([source])
            while q:
                node = q.popleft()
                for nb in adj[node]:
                    if nb not in visited:
                        subgraphs[-1].append(nb)
                        visited.add(nb)
                        q.append(nb)

        return len(subgraphs)

        