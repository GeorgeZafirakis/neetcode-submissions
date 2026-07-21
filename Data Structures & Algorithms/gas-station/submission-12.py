class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        pos = 0
        curSum = 0
        for i in range(len(gas)):
            
            diff = gas[i] - cost[i]
            curSum += diff

            if curSum < 0:
                curSum = 0
                pos = i + 1

        return pos

