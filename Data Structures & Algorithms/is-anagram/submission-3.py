class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_map = dict()

        for c in s:
            if c in freq_map:
                freq_map[c] += 1
            else:
                freq_map[c] = 1
        
        for c in t:
            if c in freq_map and freq_map[c] != 0:
                freq_map[c] -= 1
            else:
                return False
        return True
                