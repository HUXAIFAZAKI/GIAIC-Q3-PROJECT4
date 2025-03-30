def double(number):
    current_number = number
    while current_number < 100:
        print(f'The double of {current_number} is {current_number * 2}')
        current_number = current_number * 2

def main():
   user_number = int(input('Enter your number: '))
   double(user_number)


if __name__ == '__main__':
    main()