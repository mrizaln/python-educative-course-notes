# In this lesson, we are going to be solving the “Two-Sum Problem”. Let’s begin by defining the problem.
# Given an array of integers, return True or False if the array has two numbers that add up to a specific target.
# You may assume that each input would have exactly one solution.

# Solution 1: Brute force
# Complexity: time O(n²), space O(1)
def two_sum_brute_force(A, target):
    for i in range(len(A)-1):
        for j in range (i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_brute_force(A, target))
target = 20
print(two_sum_brute_force(A, target))


# Solution 2: Hash table
# Complexity: time O(n), space O(n)
def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        print(ht)
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False

target = 13
print(two_sum_hash_table(A, target))


# Solution 3: best solution
# Complexity: time O(n), space O(1)
# Note      : only works if the array is already being sorted
def two_sum(A, target):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False
    

print(two_sum(A, target))
print(two_sum(A, 20))
