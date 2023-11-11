#!/usr/bin/env python
# coding: utf-8

# ![](https://i.imgur.com/e8dC66n.png)

# In[6]:


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # it has to run in O(n) time and uses constant extra space.

        n = len(nums)

        # 1. mark numbers (num < 0) and (num > n) with a special marker number (n+1)
        # (we can ignore those because if all number are > n then we'll simply return 1)
        for i in range(n):
                if nums[i] <= 0 or nums[i] > n:
                    nums[i] = n + 1
        # note: all number in the array are now positive, and on the range 1..n+1

        # 2. mark each cell appearing in the array, by converting the index for that number to negative

        for i in range(n):
            num = abs(nums[i])
            if num > n:
                continue
            num -= 1
            if nums[num] > 0:
                nums[num] *= -1

        # 3. find the first cell which isn't negative (doesn't appear in the array)
        for i in range(n):
            if nums[i] >= 0:
                return i+1

        # 4. no positive numbers were found, which means the array contains all numbers 1..n
        return n+1

