PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = "Sorry I only tell jokes."

def main():
    while True:
        user_input: str = input(PROMPT+"\n1)Jokes\n2)Candy\n3)Money\n")
        if user_input == "1":
            print(JOKE)
            break
        elif user_input == "2":
            print("I'm sorry, but I can't give you candy.")
            break
        elif user_input == "3":
            print(SORRY)
            break

if __name__ == '__main__':
    main()