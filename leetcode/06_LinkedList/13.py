# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # 1. copy nodes

        cur = head
        while cur:
            next = cur.next # save next
            cur.next = Node(cur.val) # copy
            cur.next.next = next # link
            cur = next # move
            
        # 2. copy random
        cur = head 
        while cur: # cur.next is not None
            if cur.random: # cur.random is not None
                cur.next.random = cur.random.next # copy
            cur = cur.next.next # move

        # 3. split
        cur = head 
        new_head = head.next # new head
        while cur: # cur.next is not None
            new_cur = cur.next # new cur
            cur.next = new_cur.next # link
            if new_cur.next: # new_cur.next is not None
                new_cur.next = new_cur.next.next # link
            cur = cur.next # move 
        return new_head # return new head

# I just         
        
