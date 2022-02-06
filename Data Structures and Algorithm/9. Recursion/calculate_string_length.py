# Given a string, calculate its length.

# Iterative approach
def iterative_str_len(input_str):
    input_str_len = 0
    for i in input_str:
        input_str_len += 1
    return input_str_len

# Recursive approach
def recursive_str_len(input_str):
    if input_str == "":
        return 0
    return 1 + recursive_str_len(input_str[1:])

def main():
    input_str = "LucidProgramming"

    print(iterative_str_len(input_str))
    print(recursive_str_len(input_str))

if __name__ == "__main__":
    main()