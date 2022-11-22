import os, random, time

DISPLAY_BOARD = ['?'] * 9
GAME_PLAYED = () * 9
USER_PLAY = []
COMPUTER_PLAY = []
COMPUTER_PICK = ""
PLAYER_PICK = ""

def display_doard():
    print(f"""

        |__{DISPLAY_BOARD[0]}__|__{DISPLAY_BOARD[1]}__|__{DISPLAY_BOARD[2]}__|
        |__{DISPLAY_BOARD[3]}__|__{DISPLAY_BOARD[4]}__|__{DISPLAY_BOARD[5]}__|
        |__{DISPLAY_BOARD[6]}__|__{DISPLAY_BOARD[7]}__|__{DISPLAY_BOARD[8]}__|
    
    """)

def computer_play(xorochoose):
    return [random.randint(0, len(GAME_PLAYED)), xorochoose]

def player_play(xorochoose):
    return [int(input("Enter Position: ")), xorochoose]

# Function for user to choose either x or o
def check_X_Or_O():
    global COMPUTER_PICK, PLAYER_PICK
    PLAYER_PICK =  input("Choose X or O: ").lower()
    
    if PLAYER_PICK == 'x':
        COMPUTER_PICK = "o"
    elif PLAYER_PICK == "o":
        COMPUTER_PICK = "x"
    else:
        print("Wrong >>> Choose either x or o")
        check_X_Or_O()

# Function for computer to play
def computer_turn():
    comp = computer_play(COMPUTER_PICK)
    insert_in_list(comp[0], comp[1])
    
    
def player_turn():
    player = player_play(PLAYER_PICK)
    insert_in_list(player[0], player[1])
    
    
# Function to insert choosen x or o play into the display board
def insert_in_list(index, char):
    replace(DISPLAY_BOARD, index, char)


def check_list(list, index, player):
    if index in list and player == "computer":
        print(f"{index} has been picked")
        computer_turn()
    if index in list and player == "user":
        print(f"{index} has been picked")
        player_turn()


def menu():
    player_turn() #Computer chooses position to play
    display_doard()
    time.sleep(3) # Game waits for 3seconds to continue
    computer_turn() #Computer chooses position to play randomly
    display_doard()


def replace(arr, index, char):
    for n in range(len(arr)):
        if n == index:
            arr[n] = char
    return arr

if __name__=="__main__":
    # os.system("color 1f")
    display_doard()

    check_X_Or_O() #Player chooses either X or O
    while True:
        menu()
        print(GAME_PLAYED)
        
        



