def bisection_method(func, a, b, tol):
    i = 1
    data = []
    f_a = func(a)
    if f_a * func(b) >= 0:
        raise ValueError("The interval does not contain a root to the given function")

    while True:
        p = a + (b - a) / 2
        f_p = func(p)

        data.append([i, a, b, p, f_p])

        if f_p == 0 or (b - a) / 2 < tol:
            with open('DATA.txt', 'w') as file:
                with open('DATA.txt', 'w') as file:
                    file.write(
                        "{:<10} {:<15} {:<15} {:<20} {:<20}\n".format("Iteration", "Interval Start", "Interval End",
                                                                      "Approximate Root", "Function Value"))
                    for row in data:
                        # Use string formatting with fixed widths
                        file.write("{:<10} {:<15.6f} {:<15.6f} {:<20.6f} {:<20.6f}\n".format(*row))
            return p, i

        i += 1
        if f_p * f_a < 0:
            b = p
        else:
            a = p


def quadratic(x):
    return x ** 2 - 6 * x + 4


result = bisection_method(quadratic, 0, 4, 0.000002)
print(f"Approximate root: {result[0]:.4f}, Iterations: {result[1]}")
