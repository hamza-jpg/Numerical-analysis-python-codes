import numpy as np
int_number = 375
decimal_number = 0.814

def integer_to_binary(number: int, bit = 16):
    bits = np.zeros(bit, dtype=int)
    for i in range(bit - 1, -1, -1):
        exp = 2 ** i
        if(number / exp >= 1):
            number = number - exp
            bits[i] = 1
    bits = bits[::-1] # reversing the array
    return bits

print("This is the integer part: ", integer_to_binary(int_number))

def decimal_to_binary(number: float, bit = 16):
    bits = np.zeros(bit, dtype=int)
    for i in range(1, bit, 1):
        exp = 2 ** (-1 * i)
        if(number > exp):
            number = number - exp
            bits[i] = 1
    bits = bits[1::]
    return bits

print("This is the decimal part: ", decimal_to_binary(decimal_number))

