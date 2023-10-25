import random
from art import logo
number_list = list(range(101))
guess_number = random.choice(number_list)

print(logo)
def hard_play():
    attemps = 10
    while attemps > 0:
        user_guess = int(input("Your number guess: "))
        if user_guess > guess_number:
            print("Too high")
            print(f"Your attemps: {attemps}")
        elif user_guess < guess_number:
            print("Too low")
            print(f"Your attemps: {attemps}")
        elif user_guess == guess_number:
            print("You win")
            print(f"Right guess! Here is the number: {guess_number}")
        else:
            print("Invalid")
        attemps -= 1
    if attemps == 0:
        print("You lose")
        print(f"Your guess number: {guess_number}")

def easy_play():
    attemps = 5
    while attemps > 0:
        user_guess = int(input("Your number guess: "))
        if user_guess > guess_number:
            print("Too high")
            print(f"Your attemps: {attemps}")
        elif user_guess < guess_number:
            print("Too low")
            print(f"Your attemps: {attemps}")
        elif user_guess == guess_number:
            print("You win")
            print(f"Right guess! Here is the number: {guess_number}")
        else:
            print("Invalid")
        attemps -= 1
    if attemps == 0:
        print("You lose")
        print(f"Your guess number: {guess_number}")

game_play = input("Do you play guess number: 'easy' or 'hard'\n").lower()
if game_play == "easy":
    easy_play()
elif game_play == "hard":
    hard_play()
else:
    print("Invalid transaction")