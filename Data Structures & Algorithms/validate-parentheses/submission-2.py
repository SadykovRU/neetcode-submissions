class Solution:
    def isValid(self, s: str) -> bool:
        correspondence = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for p in s:
            if p in ('(', '{', '['):
                stack.append(p)
            else:
                if not stack or correspondence[p] != stack[-1]:
                    return False
                else:
                    stack.pop()
            
        return not stack