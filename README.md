# Numerical Analysis - Python Codes

This repository contains Python implementations, exercises, and algorithms developed for the **Numerical Analysis** course.

##  Contents

* **`numpy_array.py`**: Creates an $n \times n$ matrix of random $d$-digit integers using NumPy and replaces its centered $m \times m$ subarray with `-1`.

##  Requirements

* **Python** 3.10+
* **NumPy**

Install the required dependencies via `pip`:

```bash
python -m pip install numpy
```

##  Usage

Clone the repository and run any script directly from the terminal:

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
python numpy_array.py
```

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

## 📄 License

This project is open-source and available for educational purposes.
