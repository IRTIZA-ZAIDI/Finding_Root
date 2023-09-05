import math


class Function:
    def __init__(self, expression):
        self.expression = expression

    def __call__(self, x):
        # Evaluate the expression using the given x
        return eval(
            self.expression,
            {
                "x": x,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log,
                "exp": math.exp,
            },
        )

    def __str__(self):
        return self.expression


def bisection_method(func, a, b, tol):
    i = 1
    data = []
    errors = []  # Store relative errors for plotting
    f_a = func(a)
    if f_a * func(b) >= 0:
        raise ValueError("The interval does not contain a root to the given function")

    while True:
        p = a + (b - a) / 2
        f_p = func(p)

        data.append([i, a, b, p, f_p])

        if f_p == 0 or (b - a) / 2 < tol:
            with open("DATA.txt", "w") as file:
                with open("DATA.txt", "w") as file:
                    file.write(
                        "{:<10} {:<15} {:<15} {:<20} {:<20}\n".format(
                            "Iteration",
                            "Interval Start",
                            "Interval End",
                            "Approximate Root",
                            "Function Value",
                        )
                    )
                    for row in data:
                        # Use string formatting with fixed widths
                        file.write(
                            "{:<10} {:<15.6f} {:<15.6f} {:<20.6f} {:<20.6f}\n".format(
                                *row
                            )
                        )
            return p, i, errors

        i += 1
        if f_p * f_a < 0:
            b = p
        else:
            a = p

        if i >= 3 and len(data) >= 3:
            x_values = [row[3] for row in data[-3:]]
            relative_error = abs(x_values[2] - x_values[1]) / abs(
                x_values[1] - x_values[0]
            )

            if i >= 4:
                # p = log(Relative Error) / log(Convergence Factor)
                # Assuming 1/2 for the bisection method
                p_estimate = math.log(relative_error) / math.log(1 / 2)

                # C = abs(x_values[2] - x_values[1]) / (abs(x_values[1] - x_values[0]) ** p)
                C_estimate = abs(x_values[2] - x_values[1]) / (
                    abs(x_values[1] - x_values[0]) ** p_estimate
                )

                print(
                    f"Iteration {i}: Relative Error = {relative_error:.6f}, Estimated Order of Convergence (p) = {p_estimate:.6f}, Estimated Asymptotic Convergence Constant (C) = {C_estimate:.6f}"
                )


polynomial_func = Function("x-cos(x) ")
print(polynomial_func)
result = bisection_method(polynomial_func, 0, math.pi, 0.0001)
print(f"Approximate root: {result[0]:.4f}, Iterations: {result[1]}")
