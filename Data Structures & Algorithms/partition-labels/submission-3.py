class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        res       = []
        curSet    = set()
        curLength = 0 
        
        
        freq = {}
        for c in s:
            freq[c] = 1+ freq.get(c,0)

        
        for c in s:

            if freq.get(c,0) > 0:
                curSet.add(c)
                curLength += 1
                freq[c]   -= 1

            if freq.get(c,0) == 0:

                canClose = True

                for c in curSet:
                    if freq.get(c,0) != 0:
                        canClose = False
                    
                if canClose:    
                    res.append(curLength)
                    curLength = 0
                    curSet    = set() 

        return res


