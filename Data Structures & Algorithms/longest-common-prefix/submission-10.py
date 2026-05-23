class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        maxAllowedLen = 201
        for s in strs:
            maxAllowedLen = min(maxAllowedLen, len(s))

        for i in range(maxAllowedLen):
            for k in range(len(strs) - 1):
                if strs[k][i] != strs[k + 1][i]:
                    return strs[0][:i]

        return strs[0][:maxAllowedLen]