class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        curGas = 0
        pos = 0

        for index in range(len(gas)):
            diff = gas[index] - cost[index]
            curGas += diff
            
            # We run out of gas, so lets start from the next position
            if curGas < 0:
                curGas = 0
                pos = index + 1

        return pos
