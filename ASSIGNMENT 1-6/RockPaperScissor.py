import random

def play():
    user = str.lower(input("Enter your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors\n"))
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(f"\nComputer also choosed {computer}\n")
        print("It's a tie!\n")
        play_Again()

    if win(user, computer):
        print(f"\nComputer choosed {computer}\n")
        print("You won!\n")
        play_Again()
    else:
        print(f"\nComputer choosed {computer}\n")
        print("You lost!\n")
        play_Again()

def win(player,computer):
    if (player == 'r'  and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

def play_Again():
  choice = str.lower(input("Do you want to play again? '1' for yes, '2' for 'no':-\n"))
  if (choice == 'yes' or choice == '1'):
    print('\n')
    play()
  else:
    return False

play()