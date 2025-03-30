def main():
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))
    bc: float = math.sqrt(ab**2 + ac**2)
    print("The length of hypotenuse (BC) is: " + str(bc))

if __name__ == '__main__':
    main()