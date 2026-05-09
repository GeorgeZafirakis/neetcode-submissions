class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        freq = {}
        for card in hand:
            freq[card] = 1 + freq.get(card, 0)
        hand.sort()

        for card in hand:
            if freq[card] != 0:
                for i in range(card, card + groupSize):
                    if freq.get(i, 0) == 0:
                        return False
                    freq[i] -= 1
        return True