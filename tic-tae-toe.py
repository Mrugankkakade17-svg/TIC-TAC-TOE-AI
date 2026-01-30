import math

# Create empty board
board = [" " for _ in range(9)]

# Print the board
def print_board():
    print()
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check if board is full
def is_full():
    return " " not in board

# Minimax Algorithm
def minimax(is_maximizing):
    if check_winner("X"):
        return 1
    if check_winner("O"):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "X"

# Human Move
def human_move():
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if 0 <= move <= 8 and board[move] == " ":
            board[move] = "O"
            break
        else:
            print("Invalid move, try again.")

# Game Loop
def play_game():
    print("TIC TAC TOE AI")
    print("You are O, AI is X")
    print("Positions are from 1 to 9 as below:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    print_board()

    while True:
        human_move()
        print_board()

        if check_winner("O"):
            print("🎉 You win!")
            break
        if is_full():
            print("🤝 It's a draw!")
            break

        print("AI is making its move...")
        ai_move()
        print_board()

        if check_winner("X"):
            print("🤖 AI wins!")
            break
        if is_full():
            print("🤝 It's a draw!")
            break

# Start the game
play_game()
