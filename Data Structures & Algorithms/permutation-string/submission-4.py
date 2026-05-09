class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq1 = [0] * 26
        freq2 = [0] * 26

        for c in s1:
            freq1[ord(c) - ord('a')] += 1

        l = 0
        r = l + len(s1)

        while r <= len(s2):

            freq2 = [0] * 26
            for c in s2[l:r]:
                freq2[ord(c) - ord('a')] += 1
            
            if freq1 == freq2:
                return True

            r += 1
            l += 1

        return False


        
        