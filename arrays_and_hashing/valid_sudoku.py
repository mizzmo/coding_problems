'''Valid Sudoku

You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
'''

# First Attempt - Sets
# Time Complexity - O(n^2)
# Space Complexity - O(n)
def get_row(board, row):
        return board[row]


def get_column(board, column):
    column_array = []
    for row in board:
        column_array.append(row[column])
    return column_array
    

def get_square(board, square):
    # Get the starting row and column of the square
    start_row = (square // 3) * 3
    start_col = (square % 3) * 3
    square_array = []
    for row in range(start_row, start_row+3):
        for column in range(start_col, start_col+3):
            square_array.append(board[row][column])
    
    return square_array



class Solution0:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 x 9 Board.
        is_valid = True
        # Each Row must contain 1 - 9 without duplicates.
        for i in range(0, 9):
            row = get_row(board, i)
            counter = 0
            for value in row:
                if value.isdigit():
                    counter += 1
            # Check if the set of the row - 1 to account for period is the same as counter.
            if counter != len(set(row))-1:
                is_valid = False

        # Each Column must contain 1 - 9 without duplicates.
        for j in range(0, 9):
            column = get_column(board, j)
            counter = 0
            for value in column:
                if value.isdigit():
                    counter += 1
            # Check if the set of the row - 1 to account for period is the same as counter.
            if counter != len(set(column))-1:
                is_valid = False


        # Each 3x3 square must contain 1-9 without duplicates.
        for k in range(0, 9):
            square = get_square(board, k)
            counter = 0
            for value in square:
                if str(value).isdigit():
                    counter += 1
            # Check if the set of the square - 1 to account for '.'
            if counter != len(set(square)) - 1:
                is_valid = False

        return is_valid
    
    
# Model Solution - Hash Map
# Time Complexity - O(n^2)
# Space Complexity - O(n^2)
class SolutionM:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True