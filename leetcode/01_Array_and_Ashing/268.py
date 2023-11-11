class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # 1. sort the array
        nums.sort()

        # 2. check if the first element is not 0
        if nums[0] != 0:
            return 0

        # 3. check if the last element is not n
        elif nums[-1] != len(nums):
            return len(nums)

        # 4. check if the element is missing somewhere in the middle
        else:
            for i in range(1, len(nums)):
                if nums[i] != nums[i-1] + 1:
                    return nums[i-1] + 1

                    
        
        
