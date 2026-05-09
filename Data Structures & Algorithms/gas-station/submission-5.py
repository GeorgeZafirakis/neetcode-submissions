class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        res = -1
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            if diff < 0:
                continue
            else:
                res    = i
                curSum = 0
                for j in range(i,  len(gas)):
                    diff = gas[j] - cost[j]
                    curSum += diff
                    if curSum < 0:
                        res = -1
                        break
                for j in range(0, i + 1):
                    diff = gas[j] - cost[j]
                    curSum += diff
                    if curSum < 0:
                        res = -1
                        break
                if res != -1:
                    return res
        return res
