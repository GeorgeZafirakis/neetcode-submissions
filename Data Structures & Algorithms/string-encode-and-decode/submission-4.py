class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res = res + str(len(s)) + "$" + s
        return res

    def decode(self, s: str) -> List[str]:

        res = []
        index = 0

        while index < len(s):
            
            start = index
            end   = index
            while s[end] != "$" and end <= len(s):
                end = end + 1
            num = int(s[start:end])
            res.append(s[end+1 : end+1+num])
            index = end+1+num

        return res