class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set()
        for num in nums:
            seen.add(num)

        maxSeq = 0
        for num in seen:
            seq = 0
            if (num - 1) not in seen:
                seq = 1
                maxSeq = max(maxSeq, seq)
                while (num+1) in seen:
                    seq += 1
                    num += 1
                    maxSeq = max(maxSeq, seq)
            else:
                continue

        return maxSeq