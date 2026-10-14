from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        sub_s = ""
        l = 0

        for r in range(len(s2)):
            sub_s += s2[r]
           
            if len(sub_s) == len(s1):
                if Counter(sub_s) == Counter(s1):
                    return True
                else:
                    sub_s = sub_s[1:]
                    l += 1
        
        return False
        