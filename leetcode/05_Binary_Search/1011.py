class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(capacity): # check if we can ship all weights in days, return True if we can
            day = 1 # current day
            cur = 0 # current weight
            for w in weights: 
                if cur + w > capacity: # if we can't ship all weights in days, return False
                    day += 1 # move to next day
                    cur = 0 # reset current weight
                cur += w # add current weight
            return day <= days # return True if we can ship all weights in days
        
        left, right = max(weights), sum(weights) # left is the max weight, right is the sum of all weights
        while left < right: # binary search to find the min capacity
            mid = left + (right - left) // 2 # mid is the current capacity
            if check(mid): # if we can ship all weights in days, move right to mid
                right = mid 
            else: # if we can't ship all weights in days, move left to mid + 1
                left = mid + 1 
        return left # return left or right, they are the same

        # Time Complexity: O(nlogn) where n is the length of weights
        # Space Complexity: O(1)
