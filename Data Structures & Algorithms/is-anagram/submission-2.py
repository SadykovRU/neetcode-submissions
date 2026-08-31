class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_dict = collections.Counter(s)

        for char in t:
            if char not in char_dict:
                return False
            else:
                char_dict[char] -= 1
                if char_dict[char] == 0:
                    del char_dict[char]
        return len(char_dict) == 0