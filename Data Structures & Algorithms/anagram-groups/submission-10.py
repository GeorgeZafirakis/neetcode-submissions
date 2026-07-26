class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        def histogram(s: str):

            hist = [0] * 26
            for c in s:
                hist[ord(c) - ord('a')] += 1
            return hist

        myMap = {}
        res   = []
        for s in strs:

            key = tuple(histogram(s))

            if key not in myMap:
                myMap[key] = []
                
            myMap[tuple(key)].append(s)

        for key in myMap:
            res.append(myMap[key])
        return res
