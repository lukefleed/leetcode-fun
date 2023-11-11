# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2

        head = ListNode(0) # dummy head
        cur = head # current node

        while l1 and l2: # while both lists are not empty
            if l1.val < l2.val: 
                cur.next = l1 # append l1 to the end of the merged list
                l1 = l1.next # move l1 to the next node
            else: 
                cur.next = l2 # append l2 to the end of the merged list
                l2 = l2.next # move l2 to the next node
            cur = cur.next # move cur to the next node

        cur.next = l1 or l2 # append the remaining nodes to the end of the merged list
        return head.next # return the merged list

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # find the middle node
        slow = fast = head # slow and fast pointers
        while fast.next and fast.next.next: # while fast is not at the end of the list
            slow = slow.next # move slow to the next node
            fast = fast.next.next # move fast to the next next node 
        # cut the list into two halves
        fast = slow # fast pointer is at the middle node
        slow = slow.next # slow pointer is at the next node
        fast.next = None # cut the list into two halves
        # sort each half
        left = self.sortList(head) # sort the left half 
        right = self.sortList(slow) # sort the right half 
        # merge the two halves
        return self.mergeTwoLists(left, right) 
