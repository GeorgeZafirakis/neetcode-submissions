class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        t1 = sorted(s)
        t2 = sorted(t)
        if t1 == t2:
            return True
        else: 
            return False
        