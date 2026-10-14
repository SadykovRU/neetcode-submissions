from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        sub_list = []
        ref_count = Counter(s1)
        count = {}
        l = 0

        for r in range(len(s2)):
            count[s2[r]] = 1 + count.get(s2[r], 0)
            sub_list.append(s2[r])
           
            if len(sub_list) == len(s1):
                if count == ref_count:
                    return True
                else:
                    count[s2[l]] -= 1
                    if count[s2[l]] == 0:
                        del count[s2[l]]
                    sub_list = sub_list[1:]
                    l += 1
        
        return False
        