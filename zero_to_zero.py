import numpy as np
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt

# Set precision to 50 decimal places
getcontext().prec = 50

# Calculate e with high precision
e = Decimal(1).exp()

# Calculate the minimum value
min_x = Decimal(1) / e
min_y = min_x ** min_x

print("x = 1/e ≈")
print(min_x)
print("\nMinimum value (1/e)^(1/e) ≈")
print(min_y)

# For comparison with numpy (standard precision)
print("\nFor comparison, numpy gives us:")
print(f"(1/e)^(1/e) ≈ {np.power(1/np.e, 1/np.e):.15f}")

# Creating a range of values from 1e-100 to 0.999999999999999999999
x_values_new = np.linspace(1e-100, 0.999999999999999999999, 1000)

# Calculating the values of x^x for the new range
y_values_new = np.power(x_values_new, x_values_new)

# Plotting the new values for x^x
plt.figure(figsize=(8, 6))
plt.plot(x_values_new, y_values_new, label=r"$x^x$", color='r')

# Adding labels and title
plt.xlabel("x", fontsize=12)
plt.ylabel(r"$x^x$", fontsize=12)
plt.title(r"Graph of $x^x$ from $x=10^{-100}$ to $x\approx1$", fontsize=14)
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
