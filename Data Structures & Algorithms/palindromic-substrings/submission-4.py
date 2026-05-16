class Solution:
    def countSubstrings(self, s: str) -> int:

        # seen = []
        res = 0

        for i in range(len(s)):

            # Odd Palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # seen.append(s[l:r+1])
                res += 1
                l -= 1
                r += 1

            # Even Palindrome
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # seen.append(s[l:r+1])
                res += 1
                l -= 1
                r += 1

        # print(seen)
        return res
