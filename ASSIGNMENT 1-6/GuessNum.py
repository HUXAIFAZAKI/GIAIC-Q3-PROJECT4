import random

def guess():
  random_number = random.randint(1, 10)
  guess = 0
  while guess != random_number:
    guess = int(input('Guess a number between 1 and 10: '))
    if guess < random_number:
      print('Too low!')
    elif guess > random_number:
      print('Too high!')
  print('Congratulation! You guessed the number!')

def computer_guess(x):
    feedback = ''
    while feedback != 'c':
        low = 1
        high = x
        if(low != high):
            guess = random.randint(low, high)
        else:
          guess = random.randint(1, x)
        print(f'\nComputer guessed {guess}')
        feedback = str.lower(input(f'Is {guess} high (H), low (L), or correct (C)? '))
        if(feedback == 'h'):
            high = guess - 1
        elif(guess == x and feedback != 'c'):
          print('it is correct')
          break
        elif(feedback == 'l'):
            low = guess + 1

print('Welcome to Guess The Number Game!')
print('Select your Game Mode')
print('1) Computer')
print('2) User')

mode = str(input("\nEnter your mode (1 or 2): ")).lower()

if(mode == '1' or mode == 'Computer' or mode == 'computer'):
  user_num = int(input('Enter a random number\n'))
  print('\nComputer will guess your number')
  computer_guess(user_num)
elif(mode == '2' or mode == 'User' or mode == 'user'):
  print('You will guess the computer number')
  guess()
else:
  print("Invalid Input")