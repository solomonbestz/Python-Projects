import random



player_score = 0
computer_score = 0

for n in range(10):
    player_guess = random.randint(1, 6)
    computer_guess = random.randint(1, 6)
    if player_guess > computer_guess:
        print("Player Win")
        player_score = player_score + 1
    elif computer_guess > player_guess:
        print("Computer Win")
        computer_score = computer_score + 1
    else:
        print("It was a tie!!")
    print("Player Played "+ str(player_guess))
    print("computer played "+ str(computer_guess))

print("Score:::::  Computer: "+ str(computer_score) + " - "+ str(player_score) + " : Player")