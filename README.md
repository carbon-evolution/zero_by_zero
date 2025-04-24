# Zero To Zero

A Python program that explores the function f(x) = x^x, particularly focusing on its behavior as x approaches zero.

## Description

This program:

1. Calculates the precise value of (1/e)^(1/e), which is the minimum value of the function x^x
2. Graphs the function x^x from x=10^(-100) to x≈1
3. Uses high precision decimal calculations to demonstrate numerical properties

The function x^x has an interesting mathematical property: as x approaches zero, x^x approaches 1, rather than zero as might be intuitively expected.

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- Decimal (from Python's standard library)

## Installation

```bash
pip install numpy matplotlib
```

## Usage

```bash
python zero_to_zero.py
```

This will display:
1. The value of 1/e with high precision
2. The minimum value of the function x^x, which is (1/e)^(1/e)
3. A comparison with NumPy's standard precision calculation
4. A graph of the function x^x from x=10^(-100) to x≈1

## Mathematical Background

For the function f(x) = x^x:
- The derivative f'(x) = x^x(1 + ln(x))
- Setting f'(x) = 0 gives us x = 1/e ≈ 0.368
- This is a minimum point, with the value (1/e)^(1/e) ≈ 0.692

As x approaches 0, x^x approaches 1, which can be proven using logarithms:
lim(x→0) x^x = lim(x→0) e^(x ln(x)) = e^(lim(x→0) x ln(x)) = e^0 = 1 

![image](https://github.com/user-attachments/assets/58046bd1-3b94-473c-961d-82d6cc3a67ae)
