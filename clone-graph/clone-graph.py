"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: #No tree exists
            return None

        seen = {node: Node(node.val)} # Keep track of what has been seen
        queue = [node]
        while queue: # BFS
            val = queue.pop(0)
            current = seen[val]
            for i in range(len(val.neighbors)): # Run through the neighbors
                if val.neighbors[i] not in seen: # Node not been seen before; create it, neighbor it, add to list
                    new_node = Node(val.neighbors[i].val)
                    seen[val.neighbors[i]] = new_node
                    queue.insert(0, val.neighbors[i])
                    current.neighbors.append(new_node)
                else: # Simply append seen node to current node neighbors
                    current.neighbors.append(seen[val.neighbors[i]])
        return seen[node]