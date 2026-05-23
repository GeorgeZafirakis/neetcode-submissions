class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        n1 = len(s)
        n2 = len(t)

        if n1 != n2:
            return False

        counter = [0] * 26

        for i in range(n1):

            counter[ ord(s[i]) - ord('a') ] += 1
            counter[ ord(t[i]) - ord('a') ] -= 1

        for i in range(26):
            if counter[i] != 0:
                return False
        return True

