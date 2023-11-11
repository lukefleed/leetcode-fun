class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        # The simple bruteforce solution would take n^4 time complexity here. We can do better by dividing given lists into two groups and precalculating all possible sums for the first group. Results go to a hashmap where keys are sums and values are frequencies. It will take n^2 time and space. After that, we iterate over elements of the second group, and for every pair check whether their sum can add up to zero with a sum from the first group using a hashmap.

        n, hm, res = len(nums1), defaultdict(int), 0 # 

        # Preprocessing first group
        for i in range(n):
            for j in range(n):
                hm[nums1[i] + nums2[j]] += 1

        # Processing second group 
        for k in range(n):
            for l in range(n):
                res += hm[0 - (nums3[k] + nums4[l])] # If the sum of the second group is 0, we can add up to 0 with a sum from the first group 

        return res
