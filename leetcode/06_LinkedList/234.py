# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. Find the middle node
        slow = fast = head # slow: 1 step, fast: 2 steps
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next

        # 2. Reverse the second half
        prev = None 
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        # 3. Compare the first and second half
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True

        
