def get_first_element(list):
    """Return the first element of the list."""
    print(f"first element of your list is {list[0]}")

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
    get_first_element(list)


if __name__ == '__main__':
    main()