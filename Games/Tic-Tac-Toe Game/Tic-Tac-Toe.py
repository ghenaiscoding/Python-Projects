def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print()

def check_winner(board, symbol):
    for i in range(3):
        if all(cell == symbol for cell in board[i]):
            return True
        if all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or \
       all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player} enter your move (row,col) [1-3,1-3]: ")
            row, col = map(int, move.strip().split(","))
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row-1][col-1] == " ":
                return row-1, col-1
            else:
                print("Invalid move. Try again.")
        except Exception:
            print("Invalid input. Use format row,col (e.g., 1,3)")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to 2-player Tic-Tac-Toe!")
    print_board(board)
    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if board_full(board):
            print("It's a draw!")
            break
        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()