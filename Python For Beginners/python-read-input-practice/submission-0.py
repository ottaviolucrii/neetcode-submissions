def add_two_numbers() -> int:
    str_nums = input()
    list_str_nums = str_nums.split(",")
    int_list = []

    for n in list_str_nums:
        int_list.append(int(n))
    
    num1 = int_list[0]
    num2 = int_list[1]

    return num1 + num2


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
