class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for str in strs:
            sortStr = ''.join(sorted(str))
            count[sortStr].append(str)

        res = []

        
        for val in count.values():
            res.append(val)

        return res
        