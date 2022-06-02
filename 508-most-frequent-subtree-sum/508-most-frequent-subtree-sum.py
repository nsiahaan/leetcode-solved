# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # maintain a dict to keep track of sum:frequency
        # use dfs to traverse tree
        # leaf nodes = sum
        
        sums = {}
        frequent = []
        def dfs(root):
            if root == None:
                return 0
            if root.left == None and root.right == None: # leaf
                if root.val not in sums: # add leaves to dict
                    sums[root.val] = 1
                else:
                    sums[root.val] += 1
                return root.val
            left = dfs(root.left)
            right = dfs(root.right)
            
            #print(root.val, left, right)
            temp = root.val + left + right # get sum of subtree
            if temp not in sums:
                sums[temp] = 1
            else: 
                sums[temp] += 1
            return temp
        dfs(root)
        
        max_frequency = max(sums.values())
        for value in sums:
            if sums[value] == max_frequency:
                frequent.append(value)
                
        return frequent