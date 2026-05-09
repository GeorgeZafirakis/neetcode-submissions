class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        remHand = sorted(hand)

        while remHand:
            buf = [remHand[0]]
            for _ in range(1, groupSize):
                next_card = buf[-1] + 1
                if next_card not in remHand:
                    return False
                buf.append(next_card)

            for card in buf:
                remHand.remove(card)

        return True
        
        
            
            
                

        