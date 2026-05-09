class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        freq = {}
        for card in hand:
            freq[card] = 1 + freq.get(card, 0)

        minCard = list(freq.keys())
        heapq.heapify(minCard)

        while minCard:
            first = minCard[0]
            for i in range(first, first + groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    heapq.heappop(minCard)
        return True
