import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    print("Here are your 10 random numbers :-")
    for i in range(N_NUMBERS):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print(f"Number {i+1}: {number}")
    

if __name__ == '__main__':
    main()