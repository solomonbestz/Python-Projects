import os, random

DISPLAY_BOARD = ['?'] * 9
GAME_PLAYED = [] * 9
USER_PLAY = []
COMPUTER_PLAY = []

def display_doard():
    print(f"""

        |__{DISPLAY_BOARD[0]}__|__{DISPLAY_BOARD[1]}__|__{DISPLAY_BOARD[2]}__|
        |__{DISPLAY_BOARD[3]}__|__{DISPLAY_BOARD[4]}__|__{DISPLAY_BOARD[5]}__|
        |__{DISPLAY_BOARD[6]}__|__{DISPLAY_BOARD[7]}__|__{DISPLAY_BOARD[8]}__|
    
    """)

def replace(arr, index, char):
    for n in range(len(arr)):
        if n == index:
            arr[n] = char
    return arr

if __name__=="__main__":
    # os.system("color 1f")
    display_doard()
    count = 0
    while count < 9:
        user_index = int(input("Enter Position: "))
        user_play = input("Choose X or O: ")
        replace(DISPLAY_BOARD, user_index, user_play.lower())
        GAME_PLAYED.append(user_index)
        display_doard()
        count += 1



