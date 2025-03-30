AFFIRMATION:str = "I am enough."
def main():
    user_affirmation:str = input(f"Please type the following affirmation: {AFFIRMATION}\n")
    while user_affirmation != AFFIRMATION:
        print("Sorry, that's not the affirmation.")
        user_affirmation = input(f"Please type the following affirmation: {AFFIRMATION}")
    print("Great job!")

if __name__ == '__main__':
    main()