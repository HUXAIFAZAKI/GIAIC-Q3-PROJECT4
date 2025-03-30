import random

def main():
    random_number = random.randint(0, 100)
    user_guess = int(input("Guess a number between 0 and 100: "))
    while user_guess!= random_number:
        if user_guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        user_guess = int(input("Guess again: "))
    print(f"Congratulations! You guessed the correct number {random_number}.")



if __name__ == '__main__':
    main()