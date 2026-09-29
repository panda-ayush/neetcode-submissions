class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        total = {}
        for num in nums:
            if total.get(num):
                return True
            else:
                total[num] = 1
        
        return False
        