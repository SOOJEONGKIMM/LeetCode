# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
       # head = TreeNode(val=root[0])
        
        if root.val == key:
            if not root.right: #if delnode==lastnode
                left = root.left
                return left
            else:
                right = root.right
                while right.left: 
                    right=right.left
                root.val, right.val = right.val, root.val
                
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root