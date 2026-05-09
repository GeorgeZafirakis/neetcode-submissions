class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False
        
        buf = [0] * 26
        for i in range(len(s)):
            buf[ord(s[i]) - ord('a')] += 1
            buf[ord(t[i]) - ord('a')] -= 1

        for num in buf:
            if num != 0:
                return False
        return True
