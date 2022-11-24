import os, random, time

DISPLAY_BOARD = ['?'] * 9
GAME_PLAYED = [] 
USER_PLAY = [2, 1, 4]
COMPUTER_PLAY = []
CHECK_WIN = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
COMPUTER_PICK = ""
PLAYER_PICK = ""

'''
0 1 2
3 4 5
6 7 8
'''
def display_doard():
    print(f"""

        |__{DISPLAY_BOARD[0]}__|__{DISPLAY_BOARD[1]}__|__{DISPLAY_BOARD[2]}__|
        |__{DISPLAY_BOARD[3]}__|__{DISPLAY_BOARD[4]}__|__{DISPLAY_BOARD[5]}__|
        |__{DISPLAY_BOARD[6]}__|__{DISPLAY_BOARD[7]}__|__{DISPLAY_BOARD[8]}__|
    
    """)

def computer_play(xorochoose):
    return [random.randint(0, 8), xorochoose]


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
    global GAME_PLAYED, COMPUTER_PICK
    comp = computer_play(COMPUTER_PICK)
    print(comp[0])
    print(GAME_PLAYED)

    if comp[0] in GAME_PLAYED:
        print(f"came here with {comp[0]}")
        computer_turn()
    else:
        insert_in_list(comp[0], comp[1])
        GAME_PLAYED.append(comp[0])


# Function for player to play 
def player_turn():
    player = player_play(PLAYER_PICK)
    insert_in_list(player[0], player[1])
    GAME_PLAYED.append(player[0])
    
    
# Function to insert choosen x or o play into the display board
def insert_in_list(index, char):
    replace(DISPLAY_BOARD, index, char)


def menu():
    player_turn() #Computer chooses position to play
    display_doard()
    time.sleep(3) # Game waits for 3seconds to continue
    computer_turn() #Computer chooses position to play randomly
    display_doard()

def check_win():
    true_win = []
    count = 0
    index = 0
    while count < len(CHECK_WIN):
        if USER_PLAY[index] in CHECK_WIN[count]:
            true_win.append(True)
            if index == 2:
                break
        else:
            true_win.clear()
            count += 1
            index = 0
        index += 1

def replace(arr, index, char):
    for n in range(len(arr)):
        if n == index:
            arr[n] = char
    return arr

if __name__=="__main__":
    # os.system("color 1f")
    check_win()
    display_doard()

    check_X_Or_O() #Player chooses either X or O
    while True:
        menu()
        print(GAME_PLAYED)
        
        



