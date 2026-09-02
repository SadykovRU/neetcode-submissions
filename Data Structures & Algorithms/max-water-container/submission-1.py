class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            vol = min(heights[l], heights[r]) * (r - l)
            max_vol = max(max_vol, vol)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_vol