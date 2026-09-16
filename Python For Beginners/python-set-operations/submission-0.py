from typing import List

def count_unique_words(words: List[str]) -> int:
    my_set = set(words)

    my_clean_list = list(my_set)
    count = 0
    
    if len(my_clean_list) == 0:
        return 0;
    else:
        for m in my_clean_list:
            count += 1
        return count;


# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
