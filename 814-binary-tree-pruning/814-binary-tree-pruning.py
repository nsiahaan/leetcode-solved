# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursion, delete all leaf nodes w/ 0
        ptr = root
        
        def dfs(ptr):
            if ptr == None:
                return ptr
            if ptr.left == None and ptr.right == None:
                if ptr.val == 0: # prune
                    return None
                else:
                    return ptr
                
            ptr.left = dfs(ptr.left)
            ptr.right = dfs(ptr.right)
            
            if not ptr.left and not ptr.right: # handle middle nodes that become leaves
                if ptr.val == 0:
                    return None
            
            return ptr
        
        return dfs(ptr)
    
        # base: no children (no left/right)
            # go back up
        # travel left all the way down
        # travel right all the way down