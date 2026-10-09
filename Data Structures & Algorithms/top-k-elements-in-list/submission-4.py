class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, v in count.items():
            freq[v].append(key)
        
        res = []
        for i in range(len(nums), 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
