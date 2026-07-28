class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for word in strs:
            n = len(word)
            res = res + str(n) + "$" + word
        return res


    def decode(self, s: str) -> List[str]:
        
        res = []
        n = len(s)
        i = 0
        
        while i < n:

            start = i
            while i < n and self.isNum(s[i]):
                i += 1
            end = i

            length = int(s[start:end])
            print(length)

            res.append(s[i+1:i+length+1])
            i += length + 1
        
        return res

            


    def isNum(self, c) -> bool:

        if (ord('0') <= ord(c) <= ord('9')):
            return True
        return False







