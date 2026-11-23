# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = 0
        curr_depth = 0

        def dfs(curr_root):
            nonlocal curr_depth, max_depth
            curr_depth += 1
            if not curr_root:
                return
            
            max_depth = max(max_depth, curr_depth)

            dfs(curr_root.left)
            curr_depth -= 1
            dfs(curr_root.right)
            curr_depth -= 1
        
        dfs(root)
        
        return max_depth
    
        
        
        
        