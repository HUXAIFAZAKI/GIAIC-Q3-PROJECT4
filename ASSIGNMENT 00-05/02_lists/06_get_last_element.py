def get_last_element(list):
    """Return the last element of the list."""
    print(f"last element of your list is {list[-1]}")

def get_list():
    """Get user input to create a list."""
    list = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        list.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return list

def main():
    list = get_list()
    get_last_element(list)


if __name__ == '__main__':
    main()