from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        max_len = 1

        l ,r = 0, 1
        seen = set()
        seen.add(s[l])

        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            r += 1
            max_len = max(max_len, len(seen))   
        
        return max_len
                    