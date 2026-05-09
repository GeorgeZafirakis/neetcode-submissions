class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            m = l + ((r - l) // 2)

            hours = 0
            for p in piles:
                hours += math.ceil(p / m)

            if hours <= h:
                r = m - 1      # try smaller speed
            else:
                l = m + 1      # need larger speed

        return l
        