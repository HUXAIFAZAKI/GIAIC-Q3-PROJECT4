def main():
    a: int = int(input("Please enter an integer to be divided: "))
    b: int = int(input("Please enter an integer to divide by: "))

    quotient: int = a // b
    remainder: int = a % b  
    
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

if __name__ == '__main__':
    main()
