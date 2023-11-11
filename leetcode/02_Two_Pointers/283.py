class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        n = len(nums)
        left, right = 0, 0

        while right < n: # right pointer is always ahead of left pointer
            if nums[right] != 0: # if right pointer is not zero, swap with left pointer
                nums[left], nums[right] = nums[right], nums[left] # swap
                left += 1 # move left pointer to the right 
            right += 1 # move right pointer to the right regardless of the value 

        
        return nums


