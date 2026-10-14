class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]

        while l <= r:
            if left_max < right_max:
                vol = left_max - height[l]
                left_max = max(height[l], left_max)

                if vol > 0:
                    trapped += vol
                l += 1

            else:
                vol = right_max - height[r]
                right_max = max(height[r], right_max)
                
                if vol > 0:
                    trapped += vol
                r -= 1

        return trapped
