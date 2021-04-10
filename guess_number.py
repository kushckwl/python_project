import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print('Sorry , again guess, too low')
        elif guess > random_number:
            print('Sorry, again guess, too high')
        
    print(f'Yepeee! you guess right number. you win the game!{random_number} is correct.')  
guess(100)                  