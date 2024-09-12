import random

play_again = "yes"

rand_num = random.randint(1, 10)

def InfiniteMode():
    player_guess = " "

    while player_guess != rand_num:
        player_guess = input("What is your guess: ")

        if player_guess == "q":
            print("You have quit the game.")
            break

        player_guess = int(player_guess)

        if player_guess == rand_num:
            print("You have won. Great Job!!")
            break

def ChallengeMode():
    guess = 0
    num_guesses = 5

    while guess < num_guesses:
        player_guess = int(input("What is your guess: "))
        guess += 1


        if player_guess == rand_num:
            print("You guessed correctly!!")
            break
        else:
            print(f"You guessed wrong. You have {num_guesses - guess} guesses left")
    
    if player_guess != rand_num:
        print(f"Sorry, you've used all your guesses. The correct number was {rand_num}.")



print("Would you like to play Infinite mode or Challenge mode?")
mode = input("Infinite or Challenge: ")

while mode != "infinite" or mode != "challenge":
    print("You can only choose between Infinite mode and Challenge mode.")
    mode = input("Infinite or Challenge: ")

    if mode == "infinite":
        InfiniteMode()
        break
    elif mode == "challenge":
        ChallengeMode()
        break