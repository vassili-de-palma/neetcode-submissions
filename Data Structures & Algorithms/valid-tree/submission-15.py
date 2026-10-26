class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indeg = [0 for _ in range(n)]
        for (u,v) in edges:
            adj[u].append(v)
            adj[v].append(u)
            # indeg[v] += 1
            #indeg[u] += 1

        isACyclic = True
        visited = set()
        def dfs(node, parent):
            nonlocal isACyclic
            nonlocal visited
            if node in visited: 
                isACyclic = False
                return 
            else: visited.add(node)
            for nb in adj[node]:
                if nb != parent:
                    dfs(nb, node)
        
        dfs(0, -1)
        return isACyclic and len(visited) == n
        