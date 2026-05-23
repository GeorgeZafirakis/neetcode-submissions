class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l,r = 0, len(s) - 1

        while l < r:

            leftValue  = s[l]
            rightValue = s[r]

            s[l] = rightValue
            s[r] = leftValue

            l += 1
            r -= 1

        