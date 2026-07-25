"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        myMap = {None : None}

        def dfs(node):

            # Base Case
            if node in myMap:
                return myMap[node]

            # Recursive Case
            myMap[node] = Node(node.val)
            for nei in node.neighbors:
                myMap[node].neighbors.append(dfs(nei))
            return myMap[node]

        return dfs(node)