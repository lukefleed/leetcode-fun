class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        range = []

        while l <= r:
            if nums[mid] == target:
                # check left and right till there are not equal to target
                left = mid
                right = mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                range.append(left)
                range.append(right)
                return range
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            mid = (l + r) // 2

        return [-1, -1]
        

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l, r = 0, len(nums) - 1
        range = []

        # now make it recursive
        def binarySearch(l, r, target):
            if l > r:
                return [-1, -1]
            mid = (l + r) // 2
            if nums[mid] == target:
                # check left and right till there are not equal to target
                left = mid
                right = mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                range.append(left)
                range.append(right)
                return range
            elif nums[mid] > target:
                return binarySearch(l, mid - 1, target)
            else:
                return binarySearch(mid + 1, r, target)

        return binarySearch(l, r, target)


