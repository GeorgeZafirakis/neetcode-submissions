class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        for s in strs:
            sortedWord = ''.join(sorted(s))
            res[sortedWord].append(s)
        return list(res.values())
    

    



