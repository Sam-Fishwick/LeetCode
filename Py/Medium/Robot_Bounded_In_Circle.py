#On an infinite plane, a robot initially stands at (0, 0) and faces north. 
#Note that:

#The north direction is the positive direction of the y-axis.
#The south direction is the negative direction of the y-axis.
#The east direction is the positive direction of the x-axis.
#The west direction is the negative direction of the x-axis.

#The robot can receive one of three instructions:

#"G": go straight 1 unit.
#"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
#"R": turn 90 degrees to the right (i.e., clockwise direction).

#The robot performs the instructions given in order, and repeats them forever.

#Return true if and only if there exists a circle in the plane such that the 
#robot never leaves the circle.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        faces: list[str] = ["N","E","S","W"]
        facing: int = 400
        coord: list = [0,0]

        print(f"Facing: {faces[facing%4]}")

        for instruct in instructions:
            match instruct:
                case "G": 
                    match faces[facing%4]:
                        case "N":
                            coord[1] += 1
                            print(f"Go North! coords = {coord}")
                        case "E":
                            coord[0] += 1
                            print(f"Go East! coords = {coord}")
                        case "S":
                            coord[1] -= 1
                            print(f"Go South! coords = {coord}")
                        case "W":
                            coord[0] -= 1
                            print(f"Go West! coords = {coord}")
                case "L": 
                    facing -= 1
                    print(f"Facing: {faces[facing%4]}")
                case "R": 
                    facing += 1
                    print(f"Facing: {faces[facing%4]}")
                    
        return coord == [0,0] or faces[facing%4] != "N"
