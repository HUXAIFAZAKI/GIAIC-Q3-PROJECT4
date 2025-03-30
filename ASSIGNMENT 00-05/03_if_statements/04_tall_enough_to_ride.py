MINIMUM_HEIGHT = 50 

def main():
    is_running = True
    while is_running:
        height = float(input("How tall are you? "))
        if height <= MINIMUM_HEIGHT:
            print("You're not tall enough to ride, but maybe next year!")
        else:
            print("You're tall enough to ride!")
        check_again = input("Do you want to try again? (yes/no) ")
        is_running = check_again.lower() == 'yes'


if __name__ == '__main__':
    main()