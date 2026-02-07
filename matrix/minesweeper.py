from typing import List

def updateBoard(board: List[List[str]], click: List[int]) -> List[List[str]]:
    rows, cols = len(board), len(board[0])
    r, c = click
    
    # Helper function to count adjacent mines
    def count_mines(r, c):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
        return count

    # Depth-first search to reveal squares
    def dfs(r, c):
        # Only process unrevealed empty cells.
        if board[r][c] != 'E':
            return
        
        mines_count = count_mines(r, c)
        if mines_count:
            board[r][c] = str(mines_count)
        else:
            board[r][c] = 'B'
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        dfs(nr, nc)
    
    # If the click is on a mine, game over.
    if board[r][c] == 'M':
        board[r][c] = 'X'
    else:
        dfs(r, c)
    
    return board

# Example usage:
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
