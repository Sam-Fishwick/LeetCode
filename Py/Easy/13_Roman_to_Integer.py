#Roman numerals are represented by seven different symbols: I, V, X, L, C, D 
#and M.

#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000

#For example, 2 is written as II in Roman numeral, just two ones added together.
#12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
#which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right. 
#However, the numeral for four is not IIII. Instead, the number four is written
#as IV. Because the one is before the five we subtract it making four. The same 
#principle applies to the number nine, which is written as IX. There are six 
#instances where subtraction is used:

#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.

#Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        n: int = 0
        y: str = "N/A"

        for i in range(0,len(s)):
            z: str = s[i+1] if (i < (len(s)-1)) else "N/A"

            match s[i]:
                case "I":
                    x = 0 if (z == "V") | (z == "X") else 1
                    n += x
                case "V":
                    x = 4 if y == "I" else 5
                    n += x
                case "X":
                    x = 0 if (z == "L") | (z == "C") else 9 if (y == "I") else 10
                    n += x
                case "L":
                    x = 40 if y == "X" else 50
                    n += x
                case "C":
                    x = 0 if (z == "D") | (z == "M") else 90 if (y == "X") else 100
                    n += x
                case "D":
                    x = 400 if y == "C" else 500
                    n += x
                case "M":
                    x = 900 if y == "C" else 1000
                    n += x
                case _:
                    print(f"{i}th numeral not recognised")
            
            y = s[i]
        
        return n
