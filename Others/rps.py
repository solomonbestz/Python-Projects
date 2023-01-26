import random
import time
from os import system, name

class AI:
  def __init__(self, name, game_play):
    self.name = name
    self.game_play = game_play


  def choose_play(self):
    return random.choice(list(self.game_play.values()))

AI_SCORE_COUNT = 0
PLAYER_SCORE_COUNT = 0


def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def linespace():
  for n in range(0, 10):
    print()

def say():
  clear()
  linespace()
  print('                             Rock 👊')
  time.sleep(2) 
  clear()
  linespace()
  print('                            Paper✋')
  time.sleep(2)
  clear()
  linespace()
  print('                            Scissors✌️')
  time.sleep(2)
  clear()
  linespace()
  print('                            Shoot!!')
  time.sleep(1)
  clear()
  

def menu():
  print('Welcome To RPS \nPlay With My Ai, Win and become a grandmaster')
  print('Game Rules: \n1)Enter Your Player Name \n2)Choose rock, paper or scissors \n3)Rock wins against Scissors \n4)Scissors wins against paper \n5)Paper wins against rock \n')

  option = input('Play Game? Yes or No: ')
  play_game(option)

def play_game(option):
  if option.lower() == 'yes':
    game_mode()
  else:
    print('Good Bye 😑😑😑')
    exit()

def play_again():
  option = input ('Do You Want To Play Again? Yes or No: ')
  if option.lower() == 'yes':
    menu()
  else:
    print('Good Bye 😑😑😑')
    exit()

def player_name():
  global playerName

  playerName = input('Enter Name: ')
  return playerName


def game_rps():
  rps_play = {
     '1': 'rock',
     '2': 'paper',
     '3': 'scissors'
  }
  return rps_play

def check_win(computer, player):
  if(computer == 'scissors' and player == 'paper') or (computer == 'rock' and player == 'scissors') or (computer == 'paper' and player == 'rock'):

     return 'Ai Win round'

  if(player == 'scissors' and computer == 'paper') or (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock'):
     return 'Player Win round'

  if(player == 'scissors' and computer == 'scissors') or (player == 'rock' and computer == 'rock') or (player == 'paper' and computer == 'paper'):

     return 'Tie Round'

def end_game(computer_name, computer_score, player_score):
  global playerName 

  if computer_score == 3:
    print('Game Over!!! 😁😁😁')
    print(f'{computer_name} Won!!!')
    play_again()
  elif player_score == 3:
    print('Game Over!!! 😁😁😁')
    print(f'{playerName} Won!!!')
    play_again()

def board(computer_name, computer, player):
  global playerName
  
 
  print()
  print(f'{computer_name} played: {computer}')
  print(f'{playerName} played: {player}')

def check_score(computer, player):
  global AI_SCORE_COUNT, PLAYER_SCORE_COUNT
  checkWin = check_win(computer, player)

  if checkWin == 'Ai Win round':
    AI_SCORE_COUNT += 1
    print(f'Computer Won this round')
    print()
   
  if checkWin == 'Player Win round':
    PLAYER_SCORE_COUNT += 1
    print(f'{playerName} Won this round')
    print()
    
  if checkWin == 'Tie Round':
    print('Tie!! Shoot Again')
    print()
    pass

  print(f'SCORES: Computer:{AI_SCORE_COUNT} - {PLAYER_SCORE_COUNT}:{playerName}')
  time.sleep(5)
  clear()


def game_mode():
  global playerName
  player_name()

  while True:
    play = game_rps()
   
    ai = AI('Computer', play)
    print()
    player_game = input(f'Choose \n1)Rock \n2)Paper \n3)Scissors \n\nPlay {playerName}: ')
    say()
    ai_play = ai.choose_play()
    player_play = play[player_game]

    board(ai.name, ai_play, player_play)
    check_score(ai_play, player_play)
    end_game(ai.name, AI_SCORE_COUNT, PLAYER_SCORE_COUNT)


if __name__=='__main__':
  menu()