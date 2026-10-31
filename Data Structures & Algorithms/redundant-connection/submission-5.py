class DSU:
    def __init__(self, n=0):
        self.forest = range(n)
        self.size = [0] * n
    
    def find(self, x):
        root, path = x, []
        while self.forest[root] != root:
            path.append(root)
            root = self.forest[root]
        for y in path:
            self.forest[y] = root
        return root

    
    def union(self, x, y):
        pass



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        for u, v in edges:
            root = u
            while parent[root] != root:
                root = parent[root]
            u_root = root
            root = v
            while parent[root] != root:
                root = parent[root]
            v_root = root
            if u_root == v_root:
                return [u,v]
            else:
                parent[v_root] = u_root




        