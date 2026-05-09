class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)

        for start in range(n):
            tank = 0
            completed = True

            for i in range(n):
                idx = (start + i) % n
                tank = tank + (gas[idx] - cost[idx])
                if tank < 0:
                    completed = False
                    break

            if completed:
                return start
                
        return -1