# In this lesson, given a string, we develop an algorithm to return the first occurring uppercase letter.

# Iterative approach
def find_uppercase_iterative(input_str):
    for char in input_str:
        if char.isupper():
            return char
    return "No uppercase character found"

# Recursive approach
def find_uppercase_recursive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No uppercase character found"
    return find_uppercase_recursive(input_str, idx+1)

def main():
    input_str_1 = "lucidProgramming"
    input_str_2 = "LucidProgramming"
    input_str_3 = "lucidprogramming"

    print(find_uppercase_iterative(input_str_1))
    print(find_uppercase_iterative(input_str_2))
    print(find_uppercase_iterative(input_str_3))

    print(find_uppercase_recursive(input_str_1))
    print(find_uppercase_recursive(input_str_2))
    print(find_uppercase_recursive(input_str_3))

if __name__ == "__main__":
    main()