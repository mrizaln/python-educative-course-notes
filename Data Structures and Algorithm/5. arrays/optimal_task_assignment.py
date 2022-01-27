# Assign tasks to workers so that the time it takes to complete all the tasks is minimized given a count of workers
# and an array where each element indicates the duration of a task.
# Each worker must work on exactly two tasks.

# Now let’s think of a general approach. From the above example, we know that we have to make pairs.
# If we generate all possible pairs, it would not be efficient as enumerating every possible pair would require generating n(n−1)2\frac{n(n - 1)}{2}​2​​n(n−1)​​ pairs where nnn is the number of tasks in the given array.

# Therefore, we are going to make use of a different approach, i.e., the greedy approach.
# In the greedy approach, we’ll focus on the following rule:
#    Pair the longest task with the shortest one.

A = [6, 3, 2, 7, 5, 5]

A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i])
