class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(len(prefix)):
            sub = prefix[:i + 1]

            for word in strs[1:]:
                if not word.startswith(sub):
                    return prefix[:i]

        return prefix