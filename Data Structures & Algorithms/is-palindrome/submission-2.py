class Solution:
    def isPalindrome(self, s: str) -> bool:
        buf = []

        for char in s:
            if self.isAlphaNum(char):
                buf.append(char.lower())
            else:
                continue

        text = "".join(buf)

        # check palindrome
        for i in range(len(text) // 2):
            if text[i] != text[len(text) - 1 - i]:
                return False
        return True

    def isAlphaNum(self, c: str) -> bool:
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
        
        