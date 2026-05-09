class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        bufS1 = [0] * 26
        bufS2 = [0] * 26
        for c in s1:
            bufS1[ord(c) - ord('a')] += 1

        # Initial window 
        for i in range(len(s1)):
            bufS2[ord(s2[i]) - ord('a')] += 1

        if bufS1 == bufS2:
            return True

        for i in range(len(s1), len(s2)):
            # Add right char
            bufS2[ord(s2[i]) - ord('a')] += 1
            # Remove left char
            bufS2[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if bufS1 == bufS2:
                return True

        return False

            