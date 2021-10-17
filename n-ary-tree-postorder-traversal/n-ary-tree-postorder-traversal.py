"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        node_list = []
        return self.dfs(root, node_list)
        
    def dfs(self, root: 'Node', node_list: list[int]) -> list[int]:
        if not root:
            return []
        for node in root.children:
            self.dfs(node, node_list)
        node_list.append(root.val)
        return node_list