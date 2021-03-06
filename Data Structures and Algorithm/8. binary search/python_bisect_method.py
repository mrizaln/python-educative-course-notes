# In this lesson, we will learn about a function that takes an array of sorted integers
# and a key and returns the index of the first occurrence of that key from the array.

import bisect
# The bisect module in Python! Bisect is a built-in binary search method in Python.
# It can be used to search for an element in a sorted list



# bisect_left
    # The bisect_left function finds the index of the target element. In the eventwhere duplicate entries
    # are satisfying the target element, the bisect_left function returns the left-most occurrence.

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# -10 is at index 1
print(bisect.bisect_left(A, -10))

# First occurrence of 285 is at index 6
print(bisect.bisect_left(A, 285))



# bisect_right()
    # The bisect_right function returns the insertion point which comes after, or to the right of,
    # any existing entries of the target element in the list

# Index position to right of -10 is 2.
print(bisect.bisect_right(A, -10)) 

# Index position after last occurrence of 285 is 9.
print(bisect.bisect_right(A, 285))



# bisect()
    # There is also just a regular default bisect function. This function is equivalent to bisect_right 

# Index position to right of -10 is 2. (Same as bisect_right)
print(bisect.bisect(A, -10)) 

# Index position after last occurrence of 285 is 9. (Same as bisect_right).
print(bisect.bisect(A, 285))



# insort_left() and insort_right()
    # Given that the list A is sorted, it is possible to insert elements into A so that the list
    # remains sorted. Functions insort_left and insort_right behave in a similar way to bisect_left
    # and bisect_right, only the insort functions insert at the index positions.

print(A)
bisect.insort_left(A, 108)
print(A)

bisect.insort_right(A, 108)
print(A)