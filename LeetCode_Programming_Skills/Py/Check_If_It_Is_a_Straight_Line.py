#You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
#represents the coordinate of a point. Check if these points make a straight 
#line in the XY plane.

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) < 3:
            return True

        y1: int = coordinates[0][1]
        y2: int = coordinates[1][1]
        x1: int = coordinates[0][0]
        x2: int = coordinates[1][0]

        for coord in coordinates:
            if (((coord[1]-y2)*(x2-x1)) != (coord[0]-x2)*(y2-y1)):
                return False
        return True
