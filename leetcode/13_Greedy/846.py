class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort() # O(log n)
        while hand: # O(n)
            start = hand[0] # start of the group 
            for i in range(groupSize): # O(k)
                if start + i not in hand: # if the next number is not in the hand
                    return False # then we can't make a group
                hand.remove(start + i) # remove the number from the hand
        return True # if we can make a group for all the numbers in the hand, then we can make groups for all the numbers    

# Time Complexity: O(n log n + n * k)
# Space Complexity: O(1)

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {} # hash table to store the count of each number
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys()) # list of all the numbers in the hand
        heapq.heapify(minH) # heapify the list
        while minH:
            first = minH[0] # get the smallest number in the hand
            for i in range(first, first + groupSize): # check if we can make a group of size k starting from the smallest number
                if i not in count: # if the next number is not in the hand
                    return False
                count[i] -= 1 # remove the number from the hand
                if count[i] == 0: # if the number is not in the hand anymore
                    if i != minH[0]: # if the number is not the smallest number in the hand
                        return False # then we can't make a group
                    heapq.heappop(minH) # remove the number from the hand
        return True
