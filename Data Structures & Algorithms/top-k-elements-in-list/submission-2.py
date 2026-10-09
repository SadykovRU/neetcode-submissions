class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        output = []

        for key, v in freq_map.items():
            if len(output) < k:
                heapq.heappush(output, (v, key))
            else:
                heapq.heappushpop(output, (v, key))
        
        print(output)
        result = []
        for i in range(k):
            result.append(output[i][1])

        return result
