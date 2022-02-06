# A fixed point in an array A is an index i such that A[i] is equal to i

# Linear (naive) approach
# Time O(n); Space O(1)
def find_fixed_point_linear(A):
    for i,n in enumerate(A):
        if i == n:
            return n
    return None

# Binary search(?) approach
# Time O(logn); Space O(1)
def find_fixed_point(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid -1
        else:
            return A[mid]
    return None

def main():
    # Fixed point is 3:
    A1 = [-10, -5, 0, 3, 7]

    # Fixed point is 0:
    A2 = [0, 2, 5, 8, 17]

    # No fixed point. Return "None":
    A3 = [-10, -5, 3, 4, 7, 9]
    print("Linear Approach")
    print(A1)
    print(find_fixed_point_linear(A1))
    print(A2)
    print(find_fixed_point_linear(A2))
    print(A3)
    print(find_fixed_point_linear(A3))
    print("Binary Search Approach")
    print(A1)
    print(find_fixed_point(A1))
    print(A2)
    print(find_fixed_point(A2))
    print(A3)
    print(find_fixed_point(A3))

if __name__ == "__main__":
    main()