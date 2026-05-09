class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # recompute max frequency every time
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1 # remove left character from window 
                l += 1           # move left pointer forward

            res = max(res, r - l + 1)

        return res