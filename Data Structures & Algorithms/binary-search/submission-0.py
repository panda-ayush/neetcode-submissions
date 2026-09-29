class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            curr = (l + r) // 2

            if nums[curr] > target:
                r = curr - 1
            elif nums[curr] < target:
                l = curr + 1
            else:
                return curr
        return -1
        