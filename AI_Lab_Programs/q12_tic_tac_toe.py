# Q12. Tic-Tac-Toe game (two human players)

def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")

def winner(board, mark):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    return any(all(board[i] == mark for i in line) for line in wins)

def play():
    board = [str(i) for i in range(1, 10)]
    player = "X"
    while True:
        print_board(board)
        try:
            move = int(input(f"Player {player}, choose a position (1-9): ")) - 1
        except ValueError:
            print("Enter a number from 1 to 9.")
            continue
        if move not in range(9) or board[move] in ("X", "O"):
            print("Invalid or occupied position. Try again.")
            continue
        board[move] = player
        if winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if all(cell in ("X", "O") for cell in board):
            print_board(board)
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    play()
