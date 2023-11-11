# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# elegant solution with recursion
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: # isSymmetric checks if the tree is symmetric
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool: # isMirror checks if the left and right subtrees are mirrors of each other
        if not left and not right: # if both are None
            return True
        if not left or not right: # if one is None and the other is not
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left) # check if the values are equal and the left subtree of the left tree is a mirror of the right subtree of the right tree and the right subtree of the left tree is a mirror of the left subtree of the right tree (symmetric)

# now with a queue
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: # isSymmetric checks if the tree is symmetric, iteratively
        if not root:
            return True
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if not left and not right: # if both are None
                continue
            if not left or not right: # if one is None and the other is not
                return False
            if left.val != right.val: # if the values are not equal
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True

# now with a stack
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: # isSymmetric checks if the tree is symmetric, iteratively
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            right = stack.pop()
            left = stack.pop()
            if not left and not right: # if both are None
                continue
            if not left or not right: # if one is None and the other is not
                return False
            if left.val != right.val: # if the values are not equal
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True
