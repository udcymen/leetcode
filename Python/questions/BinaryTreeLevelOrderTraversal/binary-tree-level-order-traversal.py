# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        
        if not root:
            return result
        
        queue = [root]
        
        while queue:
            new_queue = []
            val = []
            
            for node in queue:
                val.append(node.val)
                
                if node.left:
                    new_queue.append(node.left)
                    
                if node.right:
                    new_queue.append(node.right)
                
            result.append(val)
            queue = new_queue
            
        return result
        
        