class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        countS1 = [0] * 26
        for c in s1:
            countS1[ ord(c) - ord('a') ] += 1

        l, r = 0, len(s1)
        
        while r <= len(s2):

            countS2 = [0] * 26

            for c in s2[l:r]:
                countS2[ ord(c) - ord('a') ] += 1
            
            flag = True
            for i in range(26):
                if countS1[i] != countS2[i]:
                    flag = False
                    break

            if flag:
                return True

            l += 1
            r += 1
        
        return False

