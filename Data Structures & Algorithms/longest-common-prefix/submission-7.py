class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]
        
        strs = sorted(strs)
        l1 = strs[0]
        ln = strs[-1]

        for i in range(min(len(l1),len(ln))):
            if l1[i] != ln[i]:
                return l1[0:i]
        return strs[0]
