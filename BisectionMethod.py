def bisection_method(func, a, b, tol):
    i = 1
    f_a = func(a)

    if f_a * func(b) >= 0:
        raise ValueError("The interval does not contain a root to the given function")

    while True:
        p = a + (b - a) / 2
        f_p = func(p)

        if f_p == 0 or (b - a) / 2 < tol:
            return p, i

        i += 1
        if f_p * f_a < 0:
            b = p
        else:
            a = p


def quadratic(x):
    return x**2 - 6 * x + 4


result = bisection_method(quadratic, 0, 4, 0.0002)
print(f"Approximate root: {result[0]:.4f}, Iterations: {result[1]}")
