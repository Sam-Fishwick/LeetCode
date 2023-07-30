class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        moves_A: List = []
        moves_B: List = []
        winner_A_row: bool = False
        winner_A_col: bool = False
        winner_A_diag: bool = False
        winner_B_row: bool = False
        winner_B_col: bool = False
        winner_B_diag: bool = False
        
        def check_lines(moves, i):
            line_0: int = 0
            line_1: int = 0
            line_2: int = 0
            for move in moves:
                match move[i]:
                    case 0: line_0 += 1
                    case 1: line_1 += 1
                    case 2: line_2 += 1
                    case _: pass
            print(f"{i}: 0 = {line_0}, 1 = {line_1}, 2 = {line_2}")
            if ((line_0 == 3) | (line_1 == 3) | (line_2 == 3)):
                return True
            else:
                return False

        def check_diagonal(moves):
            diagonal_back: int = 0
            diagonal_forward: int = 0
            for move in moves:
                if move[0] == move[1]:
                    diagonal_back += 1
                    if move[0] == 1:
                        diagonal_forward += 1
                elif (sum(move)) == 2:
                    diagonal_forward += 1
            return True if ((diagonal_back == 3) | (diagonal_forward == 3)) else False

        def split_moves(moves):
            for i, move in enumerate(moves):
                moves_A.append(move) if i % 2 == 0 else moves_B.append(move)
        
        split_moves(moves)
        print(f"A = {moves_A}\nB = {moves_B}")
        winner_A_row = check_lines(moves_A, 0)
        winner_B_row = check_lines(moves_B, 0)
        winner_A_col = check_lines(moves_A, 1)
        winner_B_col = check_lines(moves_B, 1)
        winner_A_diag = check_diagonal(moves_A)
        winner_B_diag = check_diagonal(moves_B)
        print(f"A: row = {winner_A_row}, col = {winner_A_col}, diag = {winner_A_diag}")
        print(f"B: row = {winner_B_row}, col = {winner_B_col}, diag = {winner_B_diag}")
        
        
        if winner_A_row | winner_A_col | winner_A_diag:
            return "A" 
        elif winner_B_row | winner_B_col | winner_B_diag:
            return "B"
        elif len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
