# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compareNode(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if node1 is None and node2 is None:
                return True
            if node1 is None:
                return False
            if node2 is None:
                return False
            if node1.val != node2.val:
                return False
            return (compareNode(node1.left, node2.left) and compareNode(node1.right, node2.right))
        return compareNode(p, q)
        