class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            if s:
                res += str(len(s)+1) + "#" + s
            else:
                res += "1" + "#"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while s and i < len(s):
            quant = ""
            while s[i].isdigit():
                quant += s[i]
                i += 1
            if int(quant) == 1:
                res.append("")
            else:
                res.append(s[i+1: i + int(quant)])
            i += int(quant)
        return res