import random

print("Welcome to Password Generator!\n")

alphabets = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()-_+"

length = int(input("Enter the length of the password: "))
passwords = int(input("Enter the number of passwords to generate: "))

include_alphabets = input("Include alphabets? (y/n): ").lower() in ['y','yes']
include_numbers = input("Include numbers? (y/n): ").lower() in ['y','yes']
include_symbols = input("Include symbols? (y/n): ").lower() in ['y','yes']

if not include_alphabets and not include_numbers and not include_symbols:
    print("\nYou must select at least one character type!")
else:
    characters = ""
    if include_alphabets:
        characters += alphabets + alphabets.upper()
    if include_numbers:
        characters += numbers
    if include_symbols:
        characters += symbols
    print("\nHere are your generated passwords:-")
    while(passwords != 0):
      password = "".join(random.sample(characters, length))
      print(password)
      passwords -= 1


