class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = {}
        for val in nums:
            if val in answer.keys():
                print(answer.values)
                return True
            else:
                answer[val] = 1
        return False
        