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
x_values = np.linspace(p0 - 5, p0 + 5, 1000)  # Adjust the range as needed
f_values = [sp.N(g.subs(x, val))for val in x_values]
p_values = []
iteration_numbers = []

# Open a text file for writing data
with open("FixedPointData.txt", "w") as file:
    # Format the header row
    header = (
        "Iteration".ljust(10)
        + "Successive Approximation (p)".ljust(30)
        + "Function Value (g(p))".ljust(30)
        + "Relative Error (|pn+1-pn| / |pn+1|)\n"
    )
    file.write(header)

    start_time = time.time()

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
            relative_error = abs(p_next - p) / abs(p_next)

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

        if abs(p_next-p) < epsilon:
            break

        p = p_next

    end_time = time.time()

    # Plot the function g(x) and iterations
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
    plt.ylabel("g(x)")
    plt.title("Fixed-Point Iteration: Function and Iterations")
    plt.legend()
    plt.grid()

    # Show the plot
    plt.show()

    # Print the result
    print(f"Root: {p_next:.15f}")
    print(f"Number of iterations: {iterations}")
    print(f"CPU time required: {end_time - start_time} seconds")

# exp(x) + 2**(-x) + 2 * cos(x) - 6
# ln(-2**(-x)-2*cos(x)+6)