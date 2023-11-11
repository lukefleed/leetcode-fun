class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        # I compute the max of the first element, the max of the array without the first element, and the max of the array without the last element. I do also the max of the first element because if the array has only one element, I have to return it.

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
