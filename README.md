# Numerical Analysis - Python Codes

This repository contains Python implementations, exercises, and algorithms developed for the **Numerical Analysis** course.

## Project Structure

```text
Numerical-analysis-python-codes/
├── src/
│   ├── IEEE754.py
│   ├── main.py
│   ├── numpy_array.py
│   └── real_to_binary_converter.py
├── LICENSE
└── README.md
```

## Contents

All scripts live in the `src/` folder.

* **`IEEE754.py`**: `IEEE754` class that converts a positive real number into the **16-bit IEEE 754 half-precision** format (1 sign bit, 5 exponent bits with bias 15, 10 mantissa bits).
  * `integer2binary` / `decimal2binary`: static helpers that convert the integer and fractional parts into NumPy bit arrays (the fractional part is limited to 10 bits).
  * Attributes: `sign_bit`, `integer_part`, `decimal_part`, `exponent_part`.
  * `print(obj)` shows the full 16-bit pattern as `sign|exponent|mantissa`, with the leading `1` of the normalized number left out of the mantissa.
* **`main.py`**: Entry point that builds an `IEEE754` object for `13.375` and prints its integer, decimal and exponent bits along with the final 16-bit representation.
* **`numpy_array.py`**: Creates an $n \times n$ matrix of random $d$-digit integers using NumPy and replaces its centered $m \times m$ subarray with `-1`.
* **`real_to_binary_converter.py`**: Converts integer (`integer_to_binary`), fractional/decimal (`decimal_to_binary`), and real floating-point numbers (`real_to_binary`) into fixed-point binary bit arrays using NumPy and `math.modf`.

## Requirements

* **Python** 3.10+
* **NumPy**

Install the required dependencies via `pip`:

```bash
python -m pip install numpy
```

## Usage

Clone the repository and run any script directly from the terminal:

```bash
git clone https://github.com/hamza-jpg/Numerical-analysis-python-codes.git
cd Numerical-analysis-python-codes
python src/main.py
python src/numpy_array.py
python src/real_to_binary_converter.py
```

### Example Output (`main.py`)

$13.375 = 1101.011_2 = 1.101011 \times 2^3$, so the stored exponent is $3 + 15 = 18 = 10010_2$:

```text
Integer part:  [1 1 0 1]
Decimal part:  [0 1 1]
Exponent part:  [1 0 0 1 0]
[0|1|0|0|1|0|1|0|1|0|1|1|0|0|0|0]
```

| Sign | Exponent | Mantissa     |
|------|----------|--------------|
| `0`  | `10010`  | `1010110000` |

### Example Output (`numpy_array.py`)

```text
Original array: 5 by 5:
[[42 17 89 34 56]
 [12 75 23 91 48]
 [64 38 10 52 79]
 [29 84 61 15 93]
 [50 19 47 82 31]]

Changed array: replaced by -1 from mid to 3 by 3 
[[42 17 89 34 56]
 [12 -1 -1 -1 48]
 [64 -1 -1 -1 79]
 [29 -1 -1 -1 93]
 [50 19 47 82 31]]
```

### Example Output (`real_to_binary_converter.py`)

```text
This is the integer part:  [0 0 0 0 0 0 0 1 0 1 1 1 0 1 1 1]
This is the decimal part:  [1 1 0 1 0 0 0 0 0 1 1 0 0 0 1]
[0 0 0 0 0 0 0 1 0 1 1 1 0 1 1 1] , [1 1 0 1 0 0 0 0 0 1 1 0 0 0 1]
```

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).
