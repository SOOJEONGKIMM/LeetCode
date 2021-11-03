# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        current=0
        sum=[0]
        self.calSum(root, current, sum)
        return sum[0]
    def calSum(self, root, current, sum):
        if not root:
            return
        current=current*10+root.val
        if not root.left and not root.right:
            sum[0]+=current
            return
        
        self.calSum(root.left, current, sum)
        self.calSum(root.right,current, sum)  