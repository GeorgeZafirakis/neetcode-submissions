class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        word = strs[0]
        for i in range(len(word)):
            sub = word[0:i+1]
            for cand in strs[1:]:
                if not sub in cand:
                    return res
            res = "".join(sub)

        return res