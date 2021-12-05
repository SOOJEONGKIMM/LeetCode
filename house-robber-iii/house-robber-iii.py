# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.rob_tree(root)
        return max(res[0],res[1])
    
    def rob_tree(self, root):
        if root is None:
            return [0,0]
        left = self.rob_tree(root.left)
        right = self.rob_tree(root.right)
        
        res=[0,0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        
        return res