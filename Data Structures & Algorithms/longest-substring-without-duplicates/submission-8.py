from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 1

        l = 0
        seen = set()
        seen.add(s[l])

        for r in range(1, len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            max_len = max(max_len, len(seen))   
        
        return max_len
                    