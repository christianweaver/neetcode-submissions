# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = [[]]
        lvl = 0
        
        def populateList(curr):
            nonlocal res, lvl

            if not curr:
                return
            
            if lvl > len(res) - 1:
                res.append([])
            
            res[lvl].append(curr.val)

            lvl += 1
            populateList(curr.left)
            populateList(curr.right)
            lvl -= 1

        populateList(root)
        return res