# Given a string, write a function to check if it is a permutation of a palindrome.

# Palindrome : A word or phrase that is the same forwards and backward.
# Permutation: A rearrangement of letters.

# A string that has an even length must have all even counts of characters, while strings
# that have an odd length must have exactly one character with an odd count.
# An even-length-ed string can’t have an odd number of exactly one character; otherwise,
# it wouldn’t be even. This is true since an odd number plus any set of even numbers will
# yield an odd number.

# Alternatively, an odd-length-ed string can’t have all characters with even counts,
# the sum of any number of even numbers is even. We can, therefore, say that it’s
# sufficient to be a permutation of a palindrome, that is a string can have no more than
# one character that is odd.

def is_palin_perm(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    d = dict()

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k,v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"
even = "never odd or even"

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))
print(is_palin_perm(even))