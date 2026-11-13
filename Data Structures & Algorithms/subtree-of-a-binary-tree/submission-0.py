# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(root1, root2) -> bool:
            if root1 is None and root2 is None:
                return True
            if root1 is None:
                return False
            if root2 is None:
                return False
            return (root1.val == root2.val) and compare(root1.left, root2.left) and compare(root1.right, root2.right)
        
        def search(node):
            if node is None and subRoot is None:
                return True
            if node is None:
                return False
            if node.val == subRoot.val:
                if compare(node, subRoot):
                    return True
            return search(node.left) or search(node.right)
        return search(root)
        