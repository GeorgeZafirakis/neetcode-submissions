class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        for s in strs:
            buf = [0] * 26
            for c in s:
                buf[ord(c) - ord('a')] += 1
            res[tuple(buf)].append(s)
        return list(res.values())