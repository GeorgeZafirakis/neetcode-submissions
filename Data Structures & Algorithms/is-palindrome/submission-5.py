class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlnum(s[l]):
                l += 1
            while l < r and not self.isAlnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l, r = l+1, r-1
        return True
            

        # res = ""
        # for ch in s:
        #     if self.isAlnum(ch):
        #         res += ch.lower()  

        # left, right = 0, len(res) - 1
        # while left < right:
        #     if res[left] != res[right]:
        #         return False
        #     else:
        #         left  += 1
        #         right -= 1
        # return True


    def isAlnum(self, c: str) -> bool:
        return(    ord('a') <= ord(c) <= ord('z') 
                or ord('A') <= ord(c) <= ord('Z') 
                or ord('0') <= ord(c) <= ord('9')
        )
        