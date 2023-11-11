# Naive DFS: O(n^2)

# Union-Find: O(n)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)] # 1-indexed
        rank = [1] * (len(edges) + 1)

        def find(n): 
            p = parent[n] # find parent

            while p != parent[p]: # find root
                parent[p] = parent[parent[p]] # path compression
                p = parent[p]
            return p # return root

        def union(n1, n2):
            p1, p2 = find(n1), find(n2) # find their parents 

            if p1 == p2: # if they are already connected
                return False 
            
            if rank[p1] > rank[p2]: # union by rank, p1 is the parent of p2
                parent[p2] = p1
                rank[p1] += rank[p2] # update rank, now p1 has more children
            else: # p2 is the parent of p1
                parent[p1] = p2 
                rank[p2] += rank[p1] # update rank, now p2 has more children
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2] # it's garanteed to have a cycle        
