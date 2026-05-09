class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0] * n
        # stores indices of days waiting for warmer temperature
        waiting = []

        for i in range(n):
            # While today is warmer than a previous waiting day
            while waiting and temperatures[i] > temperatures[waiting[-1]] :
                prev_day = waiting.pop()
                res[prev_day] = i - prev_day
            # Today is now waiting for a warmer day
            waiting.append(i)
        return res