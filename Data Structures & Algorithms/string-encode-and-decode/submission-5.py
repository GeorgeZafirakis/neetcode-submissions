class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []
        for word in strs:
            l1 = len(word)
            encodedWord = str(l1) + "$" + word
            res.append(encodedWord)
        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        while i < len(s): 
            start = i  
            while i < len(s) and self.isDigit(s[i]):  
                i += 1
            end = i  

            numStart  = start 
            numEnd    = end
            charIndex = end + 1 
            
            length = int(s[numStart:numEnd])  
            word = s[charIndex : charIndex + length]
            i = charIndex + length
            
            res.append(word)
        return res



    def isDigit(self, c) -> bool:
        if ord('0') <= ord(c) <= ord('9'):  
            return True
        return False