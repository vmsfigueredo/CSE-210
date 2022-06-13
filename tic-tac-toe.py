def game():
    board = ['1', '2', '3', '4', '5', '6', '7', '8','9']
    current_player = 'x';
    rounds = 0
    while(check_game(board) == False):
        draw(board)
        board = play(board, current_player)
        if current_player == 'x':
            current_player = 'o'
        else:
            current_player = 'x'
        rounds += 1
    if current_player == 'x':
        current_player = 'o'
    else:
        current_player = 'x'
    print(f"{current_player} won the game in {rounds} rounds:")
    draw(board)
    print("Good game. Thanks for playing!")

def draw(board):
    print(f"""
        {board[0]}|{board[1]}|{board[2]}
        --+--+--
        {board[3]}|{board[4]}|{board[5]}
        --+--+--
        {board[6]}|{board[7]}|{board[8]}
    """)
    return
def check_game(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
def play(board, player):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    while board[square-1] == 'x' or board[square-1] == 'o':
        square = int(input(f"This square is already selected by {board[square-1]}, please select another square (1-9): "))
    board[square-1] = player
    return board
def main():
    game()
main()