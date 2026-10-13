class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while s and i < len(s):
            quant = ""
            while s[i].isdigit():
                quant += s[i]
                i += 1
            i += 1
            res.append(s[i: i + int(quant)])
            i += int(quant)
        return res