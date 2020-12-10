# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
       
        self.sum = 0
        
        def solve(grandparent,parent):
            if grandparent != None and parent != None:
                if grandparent.val % 2 == 0:
                    if parent.left != None:
                        self.sum += parent.left.val
                    if parent.right != None:
                        self.sum += parent.right.val
                solve(parent,parent.left) #make sure whether they are Nonetype 
                solve(parent,parent.right)
            
        solve(root,root.left)
        solve(root,root.right)
        
        return self.sum
        
                    
                    
    
    
    
 
