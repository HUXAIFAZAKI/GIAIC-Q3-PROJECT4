def main():
    list = []
    value = input("Enter a value : ")
    while value:
        list.append(value)
        value = input("Enter a value or press enter to stop : ")
    print(f"Your list is {list}")

if __name__ == '__main__':
    main()
    