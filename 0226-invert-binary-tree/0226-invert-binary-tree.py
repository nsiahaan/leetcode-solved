# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:      
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive, swap left and right
        if not root: # null node
            return root
        
        # swap the children
        temp = root.left
        root.left = root.right
        root.right = temp
        
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        return root
        