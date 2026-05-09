class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # res = defaultdict(list)
        # for s in strs:
        #     sortedWord = ''.join(sorted(s))
        #     res[sortedWord].append(s)
        # return list(res.values())

        res = defaultdict(list)
        for s in strs:
            buffer = [0] * 26
            for c in s:
                buffer[ord(c) - ord('a')] += 1
            res[tuple(buffer)].append(s)
        return list(res.values())

    

    



