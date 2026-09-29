class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        opposite = {}

        for i, k in enumerate(nums):
            dif = target - k
            if(opposite.get(dif) is not None):
                return [opposite[dif], i]
            
            opposite[k] = i

        return []