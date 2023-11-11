# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf') # initialize the max sum to negative infinity
        self.max_gain(root) # call the max gain function
        return self.max_sum

    def max_gain(self, node): # returns the max gain from the node 
        if not node:
            return 0

        left_gain = max(self.max_gain(node.left), 0) # if the left gain is negative, we don't want to include it
        right_gain = max(self.max_gain(node.right), 0) # if the right gain is negative, we don't want to include it

        price_newpath = node.val + left_gain + right_gain # the price of the new path is the node value + the left gain + the right gain (the left and right gains are 0 if they are negative)

        self.max_sum = max(self.max_sum, price_newpath) # update the max sum if the new path is greater than the current max sum

        return node.val + max(left_gain, right_gain) # return the max gain from the node where the max gain is the max of the node value and the node value + the max gain of the left or right child
