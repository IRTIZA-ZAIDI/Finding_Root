import sympy as sp
import time
import matplotlib.pyplot as plt
import numpy as np

# Define the symbolic variable
x = sp.symbols("x")

# Input the equation as a string
f_expr = input("Enter the function f(x) in Pythonic format: ")

# Parse the equation string into a symbolic expression
try:
    f = sp.sympify(f_expr)
except sp.SympifyError:
    print("Invalid equation format. Please enter a valid equation.")
    exit(1)

# Calculate the derivative of f
f_prime = sp.diff(f, x)

# Input initial guess and tolerance
p0 = float(input("Enter initial guess p0: "))
epsilon = float(input("Enter tolerance ϵ: "))

# Check if the derivative is zero at the initial guess
if sp.N(f_prime.subs(x, p0)) == 0:
    print("Derivative is zero at the initial guess. Please choose a new initial guess.")
else:
    # Initialize variables
    p = p0
    iterations = 0

    # Lists to store data for plotting
    x_values = np.linspace(p0 - 5, p0 + 5, 1000)  # Adjust the range as needed
    f_values = [sp.N(f.subs(x, val)) for val in x_values]
    p_values = []
    iteration_numbers = []

    # Open a text file for writing data
    with open("NewtonData.txt", "w") as file:
        # Format the header row
        header = (
            "Iteration".ljust(10)
            + "Approximation (p)".ljust(25)
            + "Function Value (f(p))".ljust(25)
            + "Relative Error (|pn+1-p| / |pn-p|)\n"
        )
        file.write(header)

        start_time = time.time()

        while True:
            iterations += 1

            f_value = sp.N(f.subs(x, p))
            f_prime_value = sp.N(f_prime.subs(x, p))

            # Calculate the next approximation using Newton's method
            p_next = p - f_value / f_prime_value

            # Check if p_next and p are equal (to avoid division by zero)
            if p_next == p:
                relative_error = 0.0
            else:
                # Calculate the relative error
                relative_error = abs(p_next - p) / abs(p_next - p0)

            # Format the data row
            data_row = (
                str(iterations).ljust(10)
                + f"{p:.15f}".ljust(25)
                + f"{f_value:.15f}".ljust(25)
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

        # Plot the function f(x) and iterations
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, f_values, label="f(x)")
        plt.scatter(
            p_values,
            [sp.N(f.subs(x, val)) for val in p_values],
            color="red",
            marker="x",
            label="Iterations",
        )
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Newton's Method: Function and Iterations")
        plt.legend()
        plt.grid()

        # Show the plot
        plt.show()

        # Print the result
        print(f"Root: {p_next:.15f}")
        print(f"Number of iterations: {iterations}")
        print(f"CPU time required: {end_time - start_time} seconds")
