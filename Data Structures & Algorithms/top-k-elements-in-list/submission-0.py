class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = heapq.nlargest(k, freq.items(), key=lambda x: x[1])

        return [num for num, count in heap]


        
 