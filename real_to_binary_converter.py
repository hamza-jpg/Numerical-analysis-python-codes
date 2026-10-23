import numpy as np
int_number = 375

def integer_to_binary(number: int, bit = 16):
    bits = np.zeros(bit, dtype=int)
    for i in range(bit - 1, -1, -1):
        exp = 2 ** i
        if(number / exp >= 1):
            number = number - exp
            bits[i] = 1
    bits = bits[::-1]
    return bits

print(integer_to_binary(int_number))
