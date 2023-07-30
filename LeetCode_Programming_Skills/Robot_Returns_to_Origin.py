class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x: int = 0
        y: int = 0

        for move in moves:
            match move:
                case "R":
                    x += 1
                case "L":
                    x -= 1
                case "U":
                    y += 1
                case "D":
                    y -= 1
                case _:
                    pass
        
        coords: tuple = (x, y)
        
        return coords == (0, 0)
