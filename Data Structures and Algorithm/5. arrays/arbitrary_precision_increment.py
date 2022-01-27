# In this lesson, we will be considering the following:
# Given: An array of non-negative digits that represent a decimal integer.
# Problem: Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic.

# solution 1:
A = [1, 4, 9]
s = ''.join(map(str, A))
print(int(s) + 1)
# too simple i guess
# this solution turns the array into a string, then the string is converted into an integer, all to do after is add 1 to the integer

# real? solution:
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

A1 = [1, 4, 9]
A2 = [1, 9, 9, 9]

print(plus_one(A1))
print(plus_one(A2))