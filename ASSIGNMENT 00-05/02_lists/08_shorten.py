MAX_LENGTH : int = 3

def shorten(list):
    while len(list) > MAX_LENGTH:
        last_elem = list.pop()
        print(f"removed {last_elem}")

# There is no need to edit code beyond this point

def get_lst():
    list = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        list.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return list

def main():
    list = get_lst()
    shorten(list)
    print("Shortened list:", list)


if __name__ == '__main__':
    main()