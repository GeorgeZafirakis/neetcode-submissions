class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s):
            l,r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def test(s1,s2):
            if isPalindrome(s1) or isPalindrome(s2):
                return True
            return False

     
        l,r = 0, len(s) - 1
        while l < r:

            if s[l] != s[r]:
                return test(s[l:r],s[l+1:r+1])
                break

            l += 1
            r -= 1

        if r - l <= 1:
            return True

        return False



            

