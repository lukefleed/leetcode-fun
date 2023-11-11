class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # we need to sort the array to avoid duplicates
        res = [] 

        def dfs(nums, path):
            res.append(path) # add the path to the result
            for i in range(len(nums)): # iterate over the array
                if i > 0 and nums[i] == nums[i-1]: # if the current element is same as the previous element, we skip it to avoid duplicates
                    continue
                dfs(nums[i+1:], path+[nums[i]]) # call the dfs function with the remaining elements and the path with the current element
        dfs(nums, [])

        return res
