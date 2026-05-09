class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        myMap = defaultdict(list)
        for word in strs:
            freq = self.freq(word)
            myMap[tuple(freq)].append(word)

        res = []
        for freq, word in myMap.items():
            res.append(word)
        return res 

    def freq(self, s: str) -> List[int]:
        
        buf = [0] * 26
        for i in range(len(s)):
            buf[ord(s[i]) - ord('a')] += 1
        return buf