#At a lemonade stand, each lemonade costs $5. Customers are standing in a queue 
#to buy from you and order one at a time (in the order specified by bills). 
#Each customer will only buy one lemonade and pay with either a $5, $10, or $20 
#bill. You must provide the correct change to each customer so that the net 
#transaction is that the customer pays $5.

#Note that you do not have any change in hand at first.

#Given an integer array bills where bills[i] is the bill the ith customer pays, 
#return true if you can provide every customer with the correct change, or false
#otherwise.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives: int = 0
        tens: int = 0

        for customer in bills:
            match customer:
                case 5: fives += 1
                case 10:
                    tens += 1
                    if fives > 0:
                        fives -= 1
                    else:
                        return False
                case 20:
                    if fives > 0 and tens > 0:
                        fives -= 1
                        tens -= 1
                    elif fives > 2:
                        fives -= 3
                    else:
                        return False

        return True
        
