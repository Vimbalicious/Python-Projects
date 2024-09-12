import random

options = ["rock", "paper", "scissors"]

win = "You win!!"
draw = "Its a draw."
loss = "You lose!!"

wins = 0
draws = 0
losses = 0

play_again = "yes"

def Game():
    player_choice = input("Rock, Paper or Scissors: ").lower()

    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        return draw
    
    if player_choice == "rock" and computer_choice == "scissors" or player_choice == "paper" and computer_choice == "rock" or player_choice == "scissors" and computer_choice == "paper":
        return win
    
    else:
        return loss


while play_again == "yes":
    Result = Game()

    if Result == win:
        wins += 1
        print(win)

    if Result == draw:
        draws += 1
        print(draw)

    if Result == loss:
        losses += 1
        print(loss)

    play_again = input("Would you like to play again? ").lower()

print("Wins: " + str(wins))
print("Draws: " + str(draws))
print("Losses: " + str(losses))