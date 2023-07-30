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
