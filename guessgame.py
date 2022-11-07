import random

def number():
    ran_num = random.choice(list(range(0, 10)))

    guess = int(input("Enter Number: "))

    while guess != ran_num:
        if guess > ran_num or guess < ran_num:
            print(f'{guess} is greater or less than {ran_num}, try again')
            guess = int(input('Enter number: '))

    else:
        print(f'Correct {guess} is equal to {ran_num}')
    


number()
        