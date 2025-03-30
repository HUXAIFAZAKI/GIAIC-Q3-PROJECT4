def get_user_numbers():
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers

def count_numbers(num_list):
    num_dict = {}
    for num in num_list:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    for num in num_dict:
        print(f"{num}: {num_dict[num]}")

def main():
    user_numbers = get_user_numbers()
    count_numbers(user_numbers)


if __name__ == '__main__':
    main()