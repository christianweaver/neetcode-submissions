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
        
        def populateList(curr, lvl):

            if not curr:
                return
            
            if lvl > len(res) - 1:
                res.append([])
            
            res[lvl].append(curr.val)


            populateList(curr.left, lvl + 1)
            populateList(curr.right, lvl + 1)


        populateList(root, 0)
        return res