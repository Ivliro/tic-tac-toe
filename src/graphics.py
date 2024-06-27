import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for column in range(3):
        button = tk.Button(root, text="", width=10, height=3, \
                    command=lambda r=row, c=column: handle_move(r,c))
        button.grid(row=row, column=column)
        buttons[row][column] = button

tk.Label(root, text="Player X's Turn").grid(row=3, columnspan=3)

canvas = tk.Canvas(root, width=300, height=300)
#canvas.pack()

game_board = [["" for _ in range(3)] for _ in range(3)]

player_turn = "X"
def take_move(row, column):
    global player_turn
    if player_turn == "X":
        game_board[row][column] = "X"
        player_turn = "O"
    else:
        game_board[row][column] = "O"
        player_turn = "X"

    button = tk.Button(root, text=game_board[row][column], width=10, height=3)
    button.grid(row=row, column=column)

def handle_move(row, column):
    if game_board[row][column] == "":
        take_move(row, column)
        is_x_turn = player_turn == "X"
        buttons[row][column].config(text=game_board[row][column])
        if check_winner():
            tk.Label(root, text=f"Player {'O' if is_x_turn else 'X'} wins!").grid(row=3, columnspan=3)
            # end game so that player can't click on other buttons
            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(state="disabled")
        elif check_tie():
            tk.Label(root, text="Tie!").grid(row=4, columnspan=3)
        else:
            tk.Label(root, text="Player " + player_turn + "'s Turn").grid(row=3, columnspan=3)

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

root.mainloop()