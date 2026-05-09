class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for c in s1:
            freq1[ord(c) - ord('a')] += 1

        # build initial window
        for c in s2[:len(s1)]:
            freq2[ord(c) - ord('a')] += 1

        if freq1 == freq2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            # add new char (right)
            freq2[ord(s2[r]) - ord('a')] += 1

            # remove old char (left)
            freq2[ord(s2[l]) - ord('a')] -= 1
            l += 1

            if freq1 == freq2:
                return True

        return False


        
        