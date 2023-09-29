import sympy as sp
import time
import matplotlib.pyplot as plt
import numpy as np

# Define the symbolic variable
x = sp.symbols("x")

# Input the equation as a string for g(x)
g_expr = input("Enter the function g(x) in Pythonic format: ")

# Parse the equation string into a symbolic expression
try:
    g = sp.sympify(g_expr)
except sp.SympifyError:
    print("Invalid equation format. Please enter a valid equation.")
    exit(1)

# Input initial guess and tolerance
p0 = float(input("Enter initial guess p0: "))
epsilon = float(input("Enter tolerance ϵ: "))

# Initialize variables
p = p0
iterations = 0

# Lists to store data for plotting
x_values = np.linspace(p0 - 2, p0 + 2, 1000)  # Adjust the range as needed
f_values = [sp.N(g.subs(x, val)) for val in x_values]
p_values = []
iteration_numbers = []

# Open a text file for writing data
with open("FixedPointData.txt", "w") as file:
    # Format the header row
    header = (
            "Iteration".ljust(10)
            + "Successive Approximation (p)".ljust(30)
            + "Function Value (g(p))".ljust(30)
            + "Relative Error (|pn+1-pn| / |pn+1|-p0)".ljust(30)
    )
    file.write(header)

    start_time = time.time()

    p_values.append(p)
    while True:
        iterations += 1

        g_value = sp.N(g.subs(x, p))

        # Calculate the next approximation using Fixed-Point Iteration
        p_next = g_value

        # Check if p_next and p are equal (to avoid division by zero)
        if p_next == p:
            relative_error = 0.0
        else:
            # Calculate the relative error
            relative_error = abs(p_next - p) / abs(p_next - p0)

        # Format the data row
        data_row = (
                str(iterations).ljust(10)
                + f"{p:.15f}".ljust(30)
                + f"{g_value:.15f}".ljust(30)
                + f"{relative_error:.15f}\n"
        )

        # Write data to the text file
        file.write(data_row)

        # Append values for plotting
        p_values.append(p)
        iteration_numbers.append(iterations)

        if relative_error < epsilon:
            break

        p = p_next

    end_time = time.time()

# Calculate and add the asymptotic constant to the text file
with open("FixedPointData.txt", "r") as read_file:
    lines = read_file.readlines()

with open("FixedPointData.txt", "w") as write_file:
    write_file.writelines(lines)  # Remove the last line (header)
    write_file.write("Asymptotic Constant (c)\n")
    for i in range(0, len(p_values)-1):
        asymptotic_constant = abs((p_values[i+1] - p_next) / (p_next - p_values[i]))
        write_file.write(f"{asymptotic_constant:.15f}\n")

# Print the result
print(f"Root: {p_next:.15f}")
print(f"Number of iterations: {iterations}")
print(f"CPU time required: {end_time - start_time} seconds")

# Plot the function f(x) and iterations
plt.figure(figsize=(10, 6))
plt.plot(x_values, f_values, label="f(x)")
plt.scatter(
    p_values,
    [sp.N(g.subs(x, val)) for val in p_values],
    color="red",
    marker="x",
    label="Iterations",
)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Fixed Point Method: Function and Iterations")
plt.legend()
plt.grid()

# Show the plot
plt.show()

# exp(x) + 2**(-x) + 2 * cos(x) - 6
# ln(-2**(-x)-2*cos(x)+6)