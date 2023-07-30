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
