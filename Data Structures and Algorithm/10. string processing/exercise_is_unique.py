# Your task is to implement an algorithm to determine if a string has all unique characters.

# Solution 1: hash table
# time complexity  O(n)
# space complexity O(n)
def is_unique_1(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True

# Solution 2: set() function
# set() is an internal function that removes any duplicates in a string?
def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)

# Solution 3: like set() function? but self-made :>
# time complexity  O(nlogn)?
# space complexity O(1)
def is_unique_3(input_str):
    char_num = 1
    i = 1
    while i < len(input_str):
        j = 0
        while j < char_num:
            if input_str[i] == input_str[j]:
                return False
            j += 1
        char_num += 1
        i += 1
    return True

# Solution 4:
# using a sting that contains all possible alphabet
def is_unique_4(input_str):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True

uniq = "adsfkhce"
not_uniq = "Muhdafjadfmihsad"

print(is_unique_1(uniq))
print(is_unique_1(not_uniq))
print(is_unique_2(uniq))
print(is_unique_2(not_uniq))
print(is_unique_3(uniq))
print(is_unique_3(not_uniq))
print(is_unique_4(uniq))
print(is_unique_4(not_uniq))