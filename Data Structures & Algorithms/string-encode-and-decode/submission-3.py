class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            parts.append(f"{len(s)}#{s}")

        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        result = []
        idx = 0

        while idx < len(s):
            j = idx
            while s[j] != "#":
                j += 1
            
            length = int(s[idx:j]) 
            result.append(s[j + 1 : j + 1 + length])

            idx = j + 1 + length
            
        return result