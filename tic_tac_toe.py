def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    print("Tic Tac Toe Game")
    print_board(board)
    
    for _ in range(9):
        row = int(input(f"Player {current_player}, choose a row (0-2): "))
        col = int(input(f"Player {current_player}, choose a column (0-2): "))
        
        if board[row][col] != " ":
            print("This cell is already taken. Try again.")
            continue
        
        board[row][col] = current_player
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"
    
    print("It's a draw!")

# Run the game
tic_tac_toe()
