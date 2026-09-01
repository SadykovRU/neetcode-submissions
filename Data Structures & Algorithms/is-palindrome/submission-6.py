class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(s, center_i):
            j = 0
            while (center_i + j) < len(s):
                if s[center_i - j] != s[center_i + j]:
                    return False
                else:
                    j += 1
            return True
        
        # Process the original string
        sub_str = ""
        for c in s:
            if c.isalnum():
                sub_str += c.lower()
        
        if len(sub_str) <= 1:
            return True
        elif len(sub_str) == 2:
            return sub_str[0] == sub_str[1]

        # Determine the center and call the helper
        if len(sub_str) % 2 == 0:
            center_i = len(sub_str) // 2 - 1
            if sub_str[center_i] != sub_str[center_i + 1]:
                return False
            return check(sub_str[:center_i] + sub_str[center_i + 1:], center_i)
        else:
            center_i = len(sub_str) // 2
            return check(sub_str, center_i)