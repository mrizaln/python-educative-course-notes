# In this lesson, we will be given an array that is bitonically sorted, an array that
# starts off with increasing terms and then concludes with decreasing terms. In any such
# sequence, there is a “peak” element which is the largest element in the sequence.

# Notice that the sequence for this problem does not contain any duplicates.

def find_highest_number(A):
    low = 0
    high = len(A) - 1

    # require at least 3 elements for a bitonic sequence.
    if len(A) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2

        mid_left = A[mid - 1] if mid + 1 >= 0 else float("-inf")
        mid_right = A[mid + 1] if mid + 1 < len(A) else float("inf")

        if mid_left < A[mid] and A[mid] < mid_right:
            low = mid + 1
        elif mid_left > A[mid] and A[mid] > mid_right:
            high = mid - 1
        elif mid_left < A[mid] and A[mid] > mid_right:
            return A[mid]
    return None

def main():
    A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(find_highest_number(A))
    A = [1, 6, 5, 4, 3, 2, 1]
    print(find_highest_number(A))
    A = [1, 2, 3, 4, 5]
    print(find_highest_number(A))
    A = [5, 4, 3, 2, 1]
    print(find_highest_number(A))

if __name__ == "__main__":
    main()