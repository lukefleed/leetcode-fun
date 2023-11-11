class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 1. Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
        k = -1 
        for i in range(len(nums) - 1): 
            if nums[i] < nums[i + 1]: 
                k = i 

        # 2. Find the largest index l > k such that nums[k] < nums[l].
        if k != -1:
            l = -1
            for i in range(k + 1, len(nums)):
                if nums[k] < nums[i]:
                    l = i

            # 3. Swap nums[k] and nums[l].
            nums[k], nums[l] = nums[l], nums[k]

        # 4. Reverse the sub-array nums[k + 1:].
        nums[k + 1:] = nums[k + 1:][::-1]
