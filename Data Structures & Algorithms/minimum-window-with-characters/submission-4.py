from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_count = Counter(t)
        need = len(need_count)
        have_count = {}
        have = 0


        min_len = [0, float('inf')]

        l = 0

        for r in range(len(s)):
            if s[r] in need_count:
                have_count[s[r]] = 1 + have_count.get(s[r], 0)
                if have_count[s[r]] == need_count[s[r]]:
                    have += 1

            while have == need:
                if (r - l + 1) < min_len[1] - min_len[0] + 1:
                    min_len = [l, r + 1]
                if s[l] in have_count:
                    have_count[s[l]] -= 1
                    if have_count[s[l]] <  need_count[s[l]]:
                        have -= 1
                l += 1

        return s[min_len[0]:min_len[1]] if min_len != [0, float('inf')] else ""