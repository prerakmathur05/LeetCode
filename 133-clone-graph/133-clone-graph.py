"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        created={}
        def dfs(node):
            
            if node in created:
                return created[node]
            new_node=Node(node.val,[])
            created[node]=new_node
            
            for neighbor in node.neighbors:
                if neighbor:
                    new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node)