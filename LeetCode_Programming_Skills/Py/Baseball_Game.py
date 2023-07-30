#You are keeping the scores for a baseball game with strange rules. At the 
#beginning of the game, you start with an empty record.

#You are given a list of strings operations, where operations[i] is the ith 
#operation you must apply to the record and is one of the following:

#An integer x. - Record a new score of x.
#'+'. - Record a new score that is the sum of the previous two scores.
#'D'. - Record a new score that is the double of the previous score.
#'C'. - Invalidate the previous score, removing it from the record.

#Return the sum of all the scores on the record after applying all the operations.

#The test cases are generated such that the answer and all intermediate 
#calculations fit in a 32-bit integer and that all operations are valid.

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores: list = []

        for op in operations:
            if op.isdigit() | op[1:].isdigit():
                scores.append(int(op))
            else:
                match op:
                    case "+":
                        scores.append(scores[-1]+scores[-2])
                    case "D":
                        scores.append(scores[-1]*2)
                    case "C":
                        scores.pop(-1)
                    case _:
                        print(f"Operation {op} not recognised")
        
        return sum(scores)
