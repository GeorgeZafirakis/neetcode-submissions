class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + str(len(word)) + "$" + word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            wordLength = int(s[i:j])
            # Go one character after "$"
            i = j + 1
            j = i + wordLength
            word = s[i:j]
            res.append(word)
            i = j
        return res


