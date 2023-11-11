# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None

        # create two pointers and set them to the head of each list
        pA = headA 
        pB = headB

        # traverse both lists until we reach the end of both 
        while pA != pB: # if they are not equal, we have not reached the end of both lists
            pA = pA.next if pA else headB # if pA is not None, move to the next node, else set it to the head of list B
            pB = pB.next if pB else headA # if pB is not None, move to the next node, else set it to the head of list A

        return pA
        
