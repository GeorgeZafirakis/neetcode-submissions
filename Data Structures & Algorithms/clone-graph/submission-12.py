"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        myMap = { None : None }

        def dfs(node):

            if node in myMap:
                return myMap[node]

            cNode       = Node(node.val)
            myMap[node] = cNode
            
            for nei in node.neighbors:
                cNode.neighbors.append(dfs(nei))
            return myMap[node]
            


        return dfs(node) 
        