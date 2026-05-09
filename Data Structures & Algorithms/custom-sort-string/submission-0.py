class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        res = []
        for c in order:
            idx = ord(c) - ord('a')
            while count[idx]:
                res.append(c)
                count[idx] -= 1

        # add characters not in order
        for i in range(26):
            while count[i]:
                res.append(chr(i + ord('a')))
                count[i] -= 1

        return "".join(res)