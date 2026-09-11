from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = l = 0
        r = 1
        visited = set()

        if len(s) > 0:
            visited.add(s[0])
        else:
            return 0

        while r < len(s):
            if s[r] in visited:
                length = max(length, len(visited))
                while s[l] != s[r]:
                    visited.remove(s[l])
                    l += 1
                visited.remove(s[l])
                l += 1   

            visited.add(s[r])     
            r += 1

        return max(length, len(visited))
                    