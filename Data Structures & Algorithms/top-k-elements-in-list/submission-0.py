class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []

        for num in freq_map:
            if not heap or len(heap) < k:
                heapq.heappush(heap, (freq_map[num], num))
                
            elif freq_map[num] > heap[0][0]:
                heapq.heapreplace(heap, (freq_map[num], num))
        
        return [e[1] for e in heap]
