class Solution:
    def longestPalindrome(self, s: str) -> str:

        # def isPali(s):

        #     l, r = 0, len(s) -1
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True

        res = ""
        maxLen = 0

        for i in range(len(s)):

            # Odd Palindrome
            l,r = i,i
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = (r - l + 1)
                    res = s[l:r+1]
                l -= 1
                r += 1    

            # Even Palindrome
            l,r = i,i+1
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = (r - l + 1)
                    res = s[l:r+1]
                l -= 1
                r += 1  

        return res




        
        