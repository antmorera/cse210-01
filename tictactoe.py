# Anthuan Morera 

# W02 Prove: Developer - Solo Code Submission

def main():
    player_1 = next_player("")
    board = create_board()
    while not (winner(board) or draw(board)):
        display_board(board)
        make_move(player_1, board)
        player_1 = next_player(player_1)
    display_board(board)
    print("GG WP") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            print("gg")
            return False
            
    return True 
    
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player_1, board):
    square = int(input(f"{player_1}'s is choosing a tile! (1-9): "))
    board[square - 1] = player_1

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()