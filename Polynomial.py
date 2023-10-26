import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define the symbolic variable x
x = sp.symbols('x')

# Function to construct the Divided Difference Table
def DDTable(x_values, f_values):
    n = len(x_values)
    table = np.zeros((n, n))
    table[:, 0] = f_values

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_values[i + j] - x_values[i])

        # Create a nicely formatted table as a string
    table_str = f"{'x-values':<10} |"
    for j in range(n):
        table_str += f"{'D' + str(j):<15} |"
    table_str += "\n"

    for i in range(n):
        table_str += f"{x_values[i]:<10.4f} |"
        for j in range(n):
            table_str += f"{table[i][j]:<15.4f} |"
        table_str += "\n"

    # Save the table to a text file
    with open("Divided_Difference_Table.txt", 'w') as file:
        file.write(table_str)

    return table


# Function to construct the Lagrange polynomial
def Lagrange(x_values, f_values, x):
    n = len(x_values)
    result = 0
    for i in range(n):
        term = f_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result


# Function to construct the Divided Difference polynomial using DDTable
def DDPolynomial(x_values, table, x):
    n = len(x_values)
    result = table[0, 0]
    product_term = 1

    for j in range(1, n):
        product_term *= (x - x_values[j - 1])
        result += table[0, j] * product_term

    return result


# Input from the user
equation = input("Enter function to evaluate: ")  #exp(x) + 2**-x + 2*cos(x) - 6
expr = sp.sympify(equation)
a1 = float(input("Enter start of interval: "))
a2 = float(input("Enter end of interval: "))
a1 = float(a1)
a2 = float(a2)
n = int(input("Enter number of n: "))
x_values = np.linspace(a1, a2, n)
f_values = [expr.subs(x, x_val) for x_val in x_values]

# Construct the Divided Difference Table
table = DDTable(x_values, f_values)
# Symbolic representation of the polynomial
dd_poly = DDPolynomial(x_values, table, x)

# Generate additional points for plotting
x_plot = x_values
f_plot = f_values
lagrange_plot = [Lagrange(x_values, f_values, x) for x in x_plot]
dd_poly_plot = [dd_poly.subs(x, x_val).evalf() for x_val in x_plot]
print(dd_poly_plot)
error_plot = [expr.subs(x, x_val) - dd_poly.subs(x, x_val).evalf() for x_val in x_plot]

# Plot the graphs
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(x_plot, f_plot, label='f(x)', color='blue', linewidth=2)
plt.plot(x_plot, lagrange_plot, label='Lagrange Polynomial', color='green', linestyle='--')
plt.plot(x_plot, dd_poly_plot, label='Divided Difference Polynomial', color='red', linestyle='-.')
plt.plot(x_plot, error_plot, label='Error (f(x) - Pn(x))', color='purple')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Polynomial Interpolation')

plt.tight_layout()
plt.show()