class Solution:
    def isPalindrome(self, s: str) -> bool:
        simplified = []
        for char in s:
            if char.isalnum():
                simplified.append(char.lower()) 
        simplified_s = "".join(simplified)
        
        l, r = 0, len(simplified_s)-1

        while l < r:
            if simplified_s[l] != simplified_s[r]:
                return False
            l += 1
            r -= 1
        return True
