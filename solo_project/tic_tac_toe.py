#basic tic tac_toe game in python

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    # Check rows, columns and diagonals for a win

    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
        
    if all(board[i][i] ==player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def drawing(board):
    return all([cell != ' ' for row in board for cell in row])

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter your move row (1,2,3): "))
        col = int(input(f"Player {current_player}, enter your move column (1,2,3): "))
        
        if not (0<=row<=3 and 0<col<=3):
            print('Invlaid move. Try again.')
            continue

        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        
        [row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"033/[1m]Player {current_player} wins!/033/[0m]")
            break
        if drawing(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'
if __name__ == "__main__":
    tic_tac_toe()

