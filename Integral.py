import numpy as np
import sympy as sp


def lagrange_interpolation(x_values, f_values):
    """
    Compute the Lagrange interpolation polynomial for given x and f values.

    Parameters:
    - x_values (list): List of x values.
    - f_values (list): Corresponding list of function values.

    Returns:
    - sp.Expr: Lagrange interpolation polynomial.
    """
    temp_coefficients = []
    l_coefficients = []

    for i in range(len(x_values)):
        term = f"({f_values[i]})"

        for j in range(len(x_values)):
            if j == i:
                continue
            term += f" * (x - {x_values[j]}) / ({x_values[i] - x_values[j]})"

        temp_coefficients.append(term)
        l_coefficients.append(sp.expand(term))

    polynomial = sp.sympify(str(l_coefficients[0]) + ' + '.join(map(str, l_coefficients[1:])))
    return polynomial


def exercise_question_area(x_values, y_values):
    """
    Compute the area using the exercise question formula.

    Parameters:
    - x_values (list): List of x values.
    - y_values (list): Corresponding list of function values.

    Returns:
    - float: Computed area.
    """
    h = (x_values[-1] - x_values[0]) / (len(x_values) - 1)
    result = y_values[0] + y_values[-1]

    for i in range(1, len(y_values) - 1):
        result += 2 * y_values[i]

    result = (h / 2) * result
    return result


def calculate_exact_value(expr, a, b):
    """
    Calculate the exact definite integral of the expression.

    Parameters:
    - expr (sp.Expr): Sympy expression.
    - a (float): Lower limit of integration.
    - b (float): Upper limit of integration.

    Returns:
    - float: Exact integral value.
    """
    integral_result = sp.integrate(expr, (x, a, b))
    return integral_result.evalf()


def simpsons_rule(expr, a, b, n):
    """
    Calculate the definite integral using Simpson's rule.

    Parameters:
    - expr (sp.Expr): Sympy expression.
    - a (float): Lower limit of integration.
    - b (float): Upper limit of integration.
    - n (int): Number of subintervals.

    Returns:
    - float: Computed integral value.
    """
    n_values = np.linspace(a, b, (n + 1))
    h = (b - a) / n
    result = fun(expr, a) + fun(expr, b)

    for i in range(1, len(n_values) - 1):
        if (i % 3) != 0:
            result += 3 * fun(expr, n_values[i])
        else:
            result += 2 * fun(expr, n_values[i])

    result = ((3 * h) / 8) * result
    return result


def trapezoidal_rule(expr, a, b, n):
    """
    Calculate the definite integral using the Trapezoidal rule.

    Parameters:
    - expr (sp.Expr): Sympy expression.
    - a (float): Lower limit of integration.
    - b (float): Upper limit of integration.
    - n (int): Number of subintervals.

    Returns:
    - float: Computed integral value.
    """
    n_values = np.linspace(a, b, (n + 1))
    h = (b - a) / n
    result = fun(expr, a) + fun(expr, b)

    for i in range(1, len(n_values) - 1):
        result += 2 * fun(expr, n_values[i])

    result = (h / 2) * result
    return result


def fun(expression, c):
    """
    Evaluate a sympy expression at a given point.

    Parameters:
    - expression (sp.Expr): Sympy expression.
    - c (float): Point at which to evaluate the expression.

    Returns:
    - float: Result of expression evaluation.
    """
    return expression.subs(x, c)


def calculate_approximate_error(prev, curr):
    """
    Calculate the absolute approximate error.

    Parameters:
    - prev (float): Previous value.
    - curr (float): Current value.

    Returns:
    - float: Absolute approximate error.
    """
    return abs(prev - curr)


if __name__ == '__main__':
    x = sp.symbols('x')

    # User inputs
    equation = input("Enter the function to evaluate: ")  # Example: sin(x**2)
    expr = sp.sympify(equation)
    start_interval = float(input("Enter the start of the interval: "))
    end_interval = float(input("Enter the end of the interval: "))
    num_subintervals = int(input("Enter the number of subintervals: "))

    # Results
    trapezoidal_result = trapezoidal_rule(expr, start_interval, end_interval, num_subintervals)
    simpson_result = simpsons_rule(expr, start_interval, end_interval, num_subintervals)

    print(f"Approximated result from the Trapezoidal rule: {trapezoidal_result}")
    print(f"Approximated result from Simpson's rule: {simpson_result}")

    # Display results in a table
    print("{:<10} {:<15} {:<17}".format("n", "Trapezoidal", "Simpson"))

    n_values = [5, 10, 20, 50, 100]
    for n in n_values:
        trapezoidal_result = trapezoidal_rule(expr, start_interval, end_interval, n)
        simpson_result = simpsons_rule(expr, start_interval, end_interval, n)
        print("{:<10} {:<15} {:<15}".format(n, trapezoidal_result, simpson_result))

    # Given expression: f = (x + 1) ** (1 / 2)
    expression = (x + 1) ** (1 / 2)
    print(f"For {expression}:-")

    # Convert the expression to a sympy expression
    sympy_expression = sp.sympify(expression)

    # Calculate the exact value of the integral for the given expression
    exact_val = calculate_exact_value(sympy_expression, 0, 0.1)

    # List of values of n for which to compute the integrals
    n_values = [6, 36, 72, 144, 288]

    # Initialize previous results for error calculations
    prev_trapezoidal = 0
    prev_simpson = 0

    # Print header for the result table
    print("{:<10} {:<15} {:<17} {:<17} {:<17} {:<17} {:<17}".format("n", "Trapezoidal", "Simpson",
                                                                    "App-Error-Trapezoidal", "App-Error-Simpson",
                                                                    "True-Error-Trapezoidal", "True-Error-Simpson"))

    # Loop over the values of n
    for n in n_values:
        # Calculate results using Trapezoidal and Simpson's rules
        trapezoidal_result = trapezoidal_rule(sympy_expression, 0, 0.1, n)
        simpson_result = simpsons_rule(sympy_expression, 0, 0.1, n)

        # Calculate approximate errors
        app_error_trapezoidal = calculate_approximate_error(prev_trapezoidal, trapezoidal_result)
        app_error_simpson = calculate_approximate_error(prev_simpson, simpson_result)

        # Calculate true errors
        true_error_trapezoidal = exact_val - trapezoidal_result
        true_error_simpson = exact_val - simpson_result

        # Update previous results for the next iteration
        prev_trapezoidal = trapezoidal_result
        prev_simpson = simpson_result

        # Print the results for the current iteration
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(n, trapezoidal_result, simpson_result,
                                                                        app_error_trapezoidal, app_error_simpson,
                                                                        true_error_trapezoidal, true_error_simpson))

    # Given data for exercise question
    x_data1 = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84]
    y_data1 = [124, 134, 148, 156, 147, 133, 121, 109, 99, 85, 78, 89, 104, 116, 123]

    # Calculate and print the area using the trapezoidal rule for Lagrange interpolation
    print(
        f"Area from the trapezoidal rule for Lagrange interpolation: {trapezoidal_rule(lagrange_interpolation(x_data1, y_data1), 0, 84, len(x_data1) - 1)}")
