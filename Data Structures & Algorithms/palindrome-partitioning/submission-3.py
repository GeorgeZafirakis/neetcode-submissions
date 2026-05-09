class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res    = []

        def dfs(i, subset):

            # Base Case
            if i == len(s):
                res.append(subset.copy())
                return

            # Recursive Case
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    subset.append(s[i:j+1])
                    dfs(j+1, subset)
                    subset.pop()

        dfs(0, [])
        return res
        

    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True