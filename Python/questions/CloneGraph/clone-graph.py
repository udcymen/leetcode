class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    nodeDict = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        return self.cloneNode(node)
        
    def cloneNode(self, node: 'Node') -> 'Node':
        newNode = Node(node.val)
        self.nodeDict[node] = newNode
        
        if node.neighbors:
            for neighbor in node.neighbors:
                if neighbor not in self.nodeDict:
                    self.nodeDict[neighbor] = self.cloneNode(neighbor)
                
                newNode.neighbors.append(self.nodeDict[neighbor]) 
                
        return newNode