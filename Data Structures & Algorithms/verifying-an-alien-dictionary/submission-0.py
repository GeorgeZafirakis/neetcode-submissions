class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(min(len(w1), len(w2))):

                if order.index(w1[j]) < order.index(w2[j]):
                    break

                if order.index(w1[j]) > order.index(w2[j]):
                    return False

            else:
                # Handles prefix case
                if len(w1) > len(w2):
                    return False

        return True