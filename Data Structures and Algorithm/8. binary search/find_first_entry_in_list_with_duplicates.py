# In this lesson, we will be writing a function that takes an array of sorted integers
# and a key and returns the index of the first occurrence of that key from the array.

# Iterative approach
def find(A, target):
    for i,n in enumerate(A):
        if n == target:
            return i
    return None

# Binary search approach
def find(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            if mid - 1< 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1

def main():
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    target = 108
    x = find(A, target)
    print(x)

if __name__ == "__main__":
    main()