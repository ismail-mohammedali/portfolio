"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        if node is None: 
            return None
        
        def dfs(node):
            
            if node in oldToNew: 
                return oldToNew[node]
                
            copy = Node(node.val)
            oldToNew[node]= copy

            for nai in node.neighbors: 
                copy.neighbors.append(dfs(nai))


            return copy
        return dfs(node)