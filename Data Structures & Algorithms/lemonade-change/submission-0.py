class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five, ten, twenty = 0, 0, 0

        for bill in bills:

            if bill == 5:
                five += 1

            elif bill == 10:
                
                if five == 0:
                    return False
                else:
                    ten  += 1
                    five -= 1

            elif bill == 15:

                if ten >= 1:
                    ten  -= 1
                    five += 1
                elif five >= 2:
                    five -= 2
                    ten  += 1
                else:
                    return False

            else:
                if ten >=1 and five >= 1:
                    ten  -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True

