'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []
        def travelInOrder(node):
            if not node:
                return
            travelInOrder(node.left)
            res.append(node.val)
            travelInOrder(node.right)
        
        travelInOrder(root)
        return res[k-1]


'''
Try InOrderTraversal, then easy.
'''
