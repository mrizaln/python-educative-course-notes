# In this lesson, we will be considering the “array advance game”. In this game, you are given an array of non-negative integers. For example:
# [3,3,1,0,2,0,1]
# Each number in the array represents the maximum you can advance in the array.

# Now the problem is as follows:
    # Is it possible to advance from the start of the array to the last element given that the maximum you can advance from a position is based on
    # the value of the array at the index you are currently present on?

# using for loop
def array_advance(A):
    furthest_reached = 0
    for i in range(len(A)-1):
        if i > furthest_reached: break
        furthest_reached = max(furthest_reached, A[i] + i)
    return furthest_reached >= i 

# using while loop
def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx


# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))
