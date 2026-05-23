class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if strs == []:
            return [[]]

        def histogram(s):

            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            return tuple(count)

        res = []
        histMap = { }
        
        for s in strs:
            t = histogram(s)
            if t in histMap:
                histMap[t].append(s)
            else:
                histMap[t] = [s]

        for t in histMap:
            res.append(histMap[t])
        return res 
        