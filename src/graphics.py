import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe")

for row in range(3):
    for column in range(3):
        button = tk.Button(root, text="", width=10, height=3)
        button.grid(row=row, column=column)

tk.Label(root, text="Player X's Turn").grid(row=3, columnspan=3)

canvas = tk.Canvas(root, width=300, height=300)
#canvas.pack()

game_board = [["" for _ in range(3)] for _ in range(3)]

player_turn = "X"
def take_move(row, column, player):
    global player_turn
    if player == "X":
        game_board[row][column] = "X"
        
        player_turn = "O"
    else:
        game_board[row][column] = "O"
        player_turn = "X"

    button = tk.Button(root, text=game_board[row][column], width=10, height=3)
    button.grid(row=row, column=column)

def check_winner():
    # check rows
    for row in range(3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] != "":
            return True
    # check columns
    for column in range(3):
        if game_board[0][column] == game_board[1][column] == game_board[2][column] != "":
            return True
    # check diagonals
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "":
        return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != "":
        return True
    return False

def check_tie():
    for row in range(3):
        for column in range(3):
            if game_board[row][column] == "":
                return False
    return True

take_move(0, 0, player_turn)
take_move(0, 1, player_turn)
take_move(0, 2, player_turn)
root.mainloop()