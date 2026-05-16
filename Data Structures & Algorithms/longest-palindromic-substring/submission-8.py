class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        maxLength = 0

        for i in range(len(s)):

            # Odd Palindrome
            l = i
            r = i
            while l >= 0 and r < len(s):
                
                if s[l] == s[r]:
                    window = (r - l + 1)
                    if window > maxLength:
                        maxLength = (r - l + 1)
                        res       = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break

            # Even Palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                
                if s[l] == s[r]:
                    window = (r - l + 1)
                    if window > maxLength:
                        maxLength = (r - l + 1)
                        res       = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break

        return res