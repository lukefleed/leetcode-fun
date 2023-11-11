class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # cache, hashmap of (index, total) --> # of ways

        # recursive function
        def backtrack(index, total):
            # base case
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            # check cache
            if (index, total) in dp: 
                return dp[(index, total)] # return cached value

            # recursive case: add or subtract current number 
            dp[(index, total)] = (backtrack(index+1, total+nums[index]) + 
                                 backtrack(index+1, total-nums[index]))
            return dp[(index, total)]

        return backtrack(0, 0)
