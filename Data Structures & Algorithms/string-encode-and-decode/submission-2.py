class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s))
            output += "#"
            for char in s:
                output += char

        return output 

    def decode(self, s: str) -> List[str]:
        result = []
        if not s:
            return result

        idx = 0
        length = ""

        while idx < len(s):
            if s[idx].isdigit():
                length += s[idx]
                idx += 1
            elif s[idx] == "#":
                new_str = s[idx+1 : idx + 1 + int(length)]
                result.append(new_str)

                idx += int(length) + 1
                length = ""
            
        return result