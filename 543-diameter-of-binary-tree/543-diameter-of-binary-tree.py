# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global result
        result = [0]
        
        def dfs(root):
             
            if not root: 
                return -1 
            right = dfs(root.right)
            left=dfs(root.left)
            result[0] = max(result[0],2+left+right)
            
            return 1+max(left,right)
        dfs(root)
        return result[0]
            
        