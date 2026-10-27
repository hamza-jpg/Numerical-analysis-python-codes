import numpy as np

def replace_center_with_minus_one(d: int, n: int, m: int) -> tuple:
    if m > n or d <= 0 or n < 0 or m <0:
        raise ValueError("Invalid parameter values")

    arr = np.random.randint(0, 10 ** d, size = (n, n))
    unaranged_arr = arr.copy()

    start = (n - m) // 2
    end = start + m

    arr[start:end, start: end] = -1

    return unaranged_arr, arr

original, changed = replace_center_with_minus_one(d=2, n=5, m=3)

print("Original array: 5 by 5:")
print(original)

print("\nChanged array: replaced by -1 from mid to 3 by 3 ")
print(changed)