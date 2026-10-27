import numpy as np

class IEEE754:

    def __init__(self, x):
        self.x = x
        self.sign_bit = 0 if x > 0 else 1
        self.integer_part = self.integer2binary(int(x))
        self.decimal_part = self.decimal2binary(x - int(x))
        self.exponent_part = self.integer2binary((self.integer_part.size - 1) + 15)

    def __str__(self):
        ieee754 = np.zeros(16, dtype=int)
        ieee754[0] = self.sign_bit
        mantissa = np.append(self.integer_part[1::], self.decimal_part)
        ieee754[1: 6:] = self.exponent_part
        ieee754[6: 6 + mantissa.size:] = mantissa
        return np.array2string(ieee754, separator="|")

    @staticmethod
    def integer2binary(x):
        b = np.empty((0,), dtype=int)
        while x > 1:
            b = np.append(b, np.array([x % 2]))
            x = int(x / 2)
        b = np.append(b, np.array([x]))
        b = b[::-1]
        return b

    @staticmethod
    def decimal2binary(x):
        b = np.empty((0,), dtype=int)
        i = 0
        while x > 0 and i < 10:
            x = x * 2
            b = np.append(b, np.array([int(x)]))
            x = x - int(x)
            i += 1
        return b