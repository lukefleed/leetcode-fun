class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # O(n*sum) time and O(sum) space
        if sum(nums) % 2 != 0:
            return False # odd sum cannot be partitioned

        dp = set()
        dp.add(0) # base case, we can always sum up to zero
        target = sum(nums) // 2

        for i in range(len(nums) -1, -1 , -1)):
            nextdp = set() # nextdp is the dp for the next iteration. We cannot update an object we are iterating over. I could have copied the set but that would be O(n)
            for t in dp: # go through all the possible sums that are already in the dp
                nextdp.add(t+nums[i]) # add the current number to the sum
                nextdp.add(t) # I don't want to loose the values of the old dp
            dp = nextdp # update the dp
            if target in dp: # if we can sum up to the target, we are done
                return True
        return False
