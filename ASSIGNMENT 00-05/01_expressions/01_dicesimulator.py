import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(f"You rolled a {total}!")
def main():
    dice1: int = 6
    print("dice1 in main() starts as: " + str(dice1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(dice1))

if __name__ == '__main__':
    main()