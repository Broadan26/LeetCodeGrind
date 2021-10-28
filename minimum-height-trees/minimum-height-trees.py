class Solution:
    
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges or n <= 2: # No edges exist or redundant n
            return [i for i in range(n)]
        
        # Create adjacency list
        adj = [set() for _ in range(n)]
        for v1, v2 in edges: 
            adj[v1].add(v2)
            adj[v2].add(v1)
        
        # Find the leaf vertices of the graph
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        
        # Remove leaves from the graph and find new resulting leaves
        # Remainder vertices once leaves gone are min height graphs
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                vert = adj[leaf].pop()
                adj[vert].remove(leaf)
                if len(adj[vert]) == 1: 
                    new_leaves.append(vert)
            leaves = new_leaves
        
        return leaves
    
    ''' Leaves can never be the minimum height tree
        Prune leaves from the graph to find remaining vertices'''