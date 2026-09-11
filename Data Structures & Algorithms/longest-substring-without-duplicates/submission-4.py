from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        visited = set()

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1   

            visited.add(s[r])     
            r += 1
            length = max(length, r - l)

        return length
                    