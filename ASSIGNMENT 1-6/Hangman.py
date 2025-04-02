import random

easy_words = ["apple", "chair", "dance", "happy", "water", "tiger", "bread", "smile", "light", "horse"]
medium_words = ["balloon", "garden", "thunder", "monster", "rocket", "puzzle", "castle", "blanket", "diamond", "window"]
hard_words = ["archaeology", "quarantine", "raspberry", "avalanche", "obstacle", "cryptic", "phenomenon", "whirlpool", "zephyr", "labyrinth"]

def random_word(words):
    word = random.choice(words)
    return word

def hangman():
    print("Welcome to Hangman!\n")
    print("Please choose a difficulty level:")
    print("1) Easy\n2) Medium\n3) Hard")
    difficulty = input("Enter the number of your choice: ").lower()
    if difficulty == "1" or difficulty == "easy":
        word = random_word(easy_words)
    elif difficulty == "2" or difficulty == "medium":
        word = random_word(medium_words)
    elif difficulty == "3" or difficulty == "hard":
        word = random_word(hard_words)
    else:
        print("Invalid choice. Please try again.")
        return
    word_letter = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    lives = 5

    while(lives > 0 and len(word_letter) > 0):
      print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

      word_list = [letter if letter in used_letters else "_" for letter in word]
      print("Current word: ", " ".join(word_list))

      user_letter = input("\nGuess a letter: ").lower()
      if user_letter in alphabet - used_letters:
          used_letters.add(user_letter)
          if user_letter in word_letter:
              word_letter.remove(user_letter)
              print("")
          else:
                lives = lives - 1
                print("\nYour letter,", user_letter, "is not in the word.")
      elif user_letter in used_letters:
          print("You have already used that letter. Please try again.")
      else:
          print("\nInvalid character. Please guess a letter.")
    if lives == 0:
        print("\nYou lost! The word was:", word)
    else:
        print("\nCongratulation! You guessed the word:", word)

hangman()