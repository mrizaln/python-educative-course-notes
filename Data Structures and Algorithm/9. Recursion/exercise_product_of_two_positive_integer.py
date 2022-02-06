# Given two numbers, find their product using recursion.
# In Python, we usually use the * operator to multiply two numbers,
# but you have to use recursion to solve this challenge. Make use of the hint given below.

    # 5 * 3 = 5 + 5 + 5 = 15

def recursive_multiply(x, y):
    if y < x:
        return recursive_multiply(y, x)
    if x == 0:
        return 0
    else:
        return y + recursive_multiply(x-1, y)

print(recursive_multiply(45,32))