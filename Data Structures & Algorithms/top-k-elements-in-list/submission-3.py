class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for key, v in count.items():
            freq[v].append(key)
        
        res = []
        for i in range(len(nums), 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
