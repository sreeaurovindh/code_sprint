# Example usage:

from typing import List

def updateBoard(board: List[List[str]], click: List[int]) -> List[List[str]]:
    r,c = click
    rows = len(board)
    cols = len(board[0])
    
    ## REMEMBER boundary conditions on matrix are 0 to rows -1 and 0 to cols-1
    
    def count_mines(r,c):
        count  = 0
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr ==0 and dc == 0:
                    continue
                if r+dr >0 and r+dr <= rows and c+dc > 0 and c+dc <=cols and board[r+dr][c+dc] == 'M':
                    count += 1
        return count














if __name__ == "__main__":
    board = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"]
    ]
    click = [3, 0]
    updated_board = updateBoard(board, click)
    for row in updated_board:
        print(" ".join(row))
