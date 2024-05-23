import random
from tkinter import *

def next_turn(row, col):
    global player
    if buttons[row][col]["text"] == "" and check() is False:
        if player == players[0]:
            buttons[row][col]["text"] = player
            if check() is False:
                player = players[1]
                label.config(text=(players[1]+ " turn"))
            elif check() is True:
                label.config(text=(players[0]+ " wins"))
            elif check() == "Tie":
                label.config(text=("Tie!"))
        else:
            buttons[row][col]["text"] = player
            if check() is False:
                player = players[0]
                label.config(text=(players[0]+ " turn"))
            elif check() is True:
                label.config(text=(players[1]+ " wins"))
            elif check() == "Tie":
                label.config(text=("Tie"))


def check():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="teal")
            buttons[row][1].config(bg="teal")
            buttons[row][2].config(bg="teal")
            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            buttons[0][col].config(bg="teal")
            buttons[1][col].config(bg="teal")
            buttons[2][col].config(bg="teal")
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="teal")
        buttons[1][1].config(bg="teal")
        buttons[2][2].config(bg="teal")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="teal")
        buttons[1][1].config(bg="teal")
        buttons[2][0].config(bg="teal")
        return True
    elif empty() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="orange")
        return "Tie"
    else:
        return False 
    
def empty():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] != "":
                spaces -=1
    if spaces == 0:
        return False
    else:
        return True
def new_game():
    global player 
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range (3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")
window = Tk()
window.title("Tiki-Taki_Toe")
#window.iconbitmap("C:/Users/petraru/Desktop/TicTacToe/tic.ico.ico")   
players = ["X", "O"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text=player + "turn", font=("consolas", 40))
label.pack(side="top")
reset_button = Button(text = "restart", font=("consolas", 20), command=new_game)
reset_button.pack(side="top")
frame = Frame(window)
frame.pack()
felder = []
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=("consolas", 40), width=6, height=2,
                                   command=lambda row=row, col=col: next_turn(row,col))
        buttons[row][col].grid(row=row, column=col)
        felder.append(buttons)
window.mainloop()