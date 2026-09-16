from typing import List

def contains_duplicate(words: List[str]) -> bool:
    origin = len(words)
    clean = set(words)

    test = len(clean)

    if test < origin:
        return True;
    elif origin == 0:
        return False;
    else:
        return False;

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
