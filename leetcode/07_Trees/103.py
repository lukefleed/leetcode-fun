class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right       

from collections import deque
from typing import List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root]) # queue for BFS
        result = [] # final result
        level = 0 # current level 
        while queue: # while queue is not empty
            level += 1 # increment level
            level_size = len(queue) # number of nodes in current level
            current_level = [] # list to store nodes of current level
            for _ in range(level_size): # process every node of current level
                current_node = queue.popleft() # remove node from queue
                if level % 2 == 0: # if level is even add nodes in reverse order
                    current_level.insert(0, current_node.val) # insert at beginning
                else: # if level is odd add nodes in normal order
                    current_level.append(current_node.val) # append at end
                if current_node.left: # if left child is not None, add it to queue
                    queue.append(current_node.left) 
                if current_node.right: # if right child is not None, add it to queue
                    queue.append(current_node.right)
            result.append(current_level) # append list of nodes of current level to result
        return result
      
