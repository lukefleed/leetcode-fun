class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # we know that there will be n! permutations
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]] # return a copy of the list

        for i in range(len(nums)):
            n = nums.pop(0) # remove the first element
            perms = self.permute(nums) # get all permutations of the rest of the list

            for perm in perms: 
                perm.append(n) # add the removed element to the end of each permutation
            res.extend(perms) # add all permutations to the result
            nums.append(n) # add the removed element back to the end of the list
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
