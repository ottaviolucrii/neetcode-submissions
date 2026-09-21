def add_two_numbers() -> int:
    itens = input()
    string_list = itens.split(",")
    num1 = int(string_list[0])
    num2 = int(string_list[1])

    return num1 + num2

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
