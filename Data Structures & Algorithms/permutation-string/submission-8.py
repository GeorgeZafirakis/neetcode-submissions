class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        bufS1 = [0] * 26
        for c in s1:
            bufS1[ord(c) - ord('a')] += 1

        l = 0
        while l < len(s2) - len(s1) + 1:
            bufS2 = [0] * 26
            for c in s2[l:l+len(s1)]:
                bufS2[ord(c) - ord('a')] += 1
            if bufS1 == bufS2:
                return True
            l += 1
        return False
            