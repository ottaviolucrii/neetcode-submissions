from typing import List

def read_integers() -> List[int]:
    enter = input()
    list_num = enter.split(",")
    list_new = []

    for n in list_num:
        list_new.append(int(n))
    return list_new

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
