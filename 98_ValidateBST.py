'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not( left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(node.right,node.val,right)
        
        return valid(root, float("-inf"), float("inf"))


'''
Needs logic, try dry run for this example if you don't understand the code.
[5,4,6,null,null,3,7]
'''
