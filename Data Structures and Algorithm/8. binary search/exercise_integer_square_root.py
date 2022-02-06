# You are required to write a function that takes a non-negative integer, k, and returns
# the largest integer whose square is less than or equal to the specified integer k.

# bisection method for square root
def integer_square_root(k):
    if k <= 1: return k
    if k <= 4: return 2
    
    err = 0.05
    low = 0
    high = k / 2

    while (high - low) > err:
        ylow = low * low - k
        yhigh = high * high - k
        
        mid = (high + low) / 2
        ymid = mid * mid - k
        # print(ylow, yhigh, low, high, mid)

        if ylow < 0 and ymid < 0:
            low = mid
        else:
            high = mid

    return int((high + low) / 2)    # dijadikan int karena disuruhnya gitu :>

def integer_square_root(k):
    
    low = 0
    high = k 

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid
        # print(low, mid, high, mid_squared)

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1
    
k = 300
print(integer_square_root(k))