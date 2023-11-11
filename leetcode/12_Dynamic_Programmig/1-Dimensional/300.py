class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1): # loop from the end
            for j in range(i + 1, len(nums)): # loop from i + 1 to the end
                if nums[i] < nums[j]: 
                    LIS[i] = max(LIS[i], 1 + LIS[j]) # update LIS[i] if needed
        return max(LIS)

# O(n^2) time, O(n) space

# greedy, with binary search
from bisect import bisect_left

class Solution:  
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x: # if x is larger than the last element in sub, append x because it is the largest element so far
                sub.append(x)
            else: # if x is smaller than the last element in sub, replace the first element in sub that is larger than x
                idx = bisect_left(sub, x)  # Find the index of the smallest number >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)

# Time:  O(nlogn)
