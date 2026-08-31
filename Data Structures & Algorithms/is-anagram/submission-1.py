class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = collections.Counter(s)

        for char in t:
            if char not in char_dict:
                return False
            else:
                char_dict[char] -= 1
                if char_dict[char] == 0:
                    del char_dict[char]
        return True if len(char_dict) == 0 else False