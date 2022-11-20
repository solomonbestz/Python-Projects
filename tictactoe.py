import random

GAME = [0, 1, 2, 3, 4, 5, 6, 7, 8]
PLAYER__OPTION = []
AI_OPTION = []


# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]

def display_board():
    print(f"""
       
       __{GAME[0]}__|__{GAME[1]}__|__{GAME[2]}__

       __{GAME[3]}__|__{GAME[4]}__|__{GAME[5]}__

       __{GAME[4]}__|__{GAME[7]}__|__{GAME[8]}__

    """)
    pass


def player_input():
    ask = input("Choose x or o") 

def score_board():
    pass

def play_again():
    pass

def game_menu():
    display_board()


if __name__=='__main__':
    game_menu()

