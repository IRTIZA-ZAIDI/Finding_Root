import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import sympy
from sympy import symbols, sympify, plot

x = symbols('x')


def f(x):
    return sympify(np.exp(x) + 2 ** (-x) + 2 * sympy.cos(x) - 6)


def generate_data(n, interval):
    x = np.linspace(interval[0], interval[1], n + 1)
    y = [f(val) for val in x]
    return x, y


def plot_cubic_spline(x, y, n, spline_type, color):
    cs = CubicSpline(x, y, bc_type=spline_type)
    xs = np.linspace(x[0], x[-1], 100)

    plt.plot(xs, cs(xs), label=f'{spline_type.capitalize()} Cubic Spline (n={n})', color=color)


def plot_original_polynomial(interval, color):
    xs = np.linspace(interval[0], interval[1], 100)
    ys = [f(val) for val in xs]
    plt.plot(xs, ys, '--', label='Original Polynomial', linewidth=2, color=color)


def solve_question_32():
    clampfor1 = [1, -0.67]
    clampfor2 = [3, -4]
    clampfor3 = [0.33, -1.5]
    xlist1 = [1, 2, 5, 6, 7, 8, 10, 13, 17]
    ylist1 = [3, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5]
    xlist2 = [17, 20, 23, 24, 25, 27, 27.7]
    ylist2 = [4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1]
    xlist3 = [27.7, 28, 29, 30]
    ylist3 = [4.1, 4.3, 4.1, 3.0]

    plt.figure(figsize=(10, 6))

    plot_cubic_spline(xlist1, ylist1, len(xlist1) - 1, "clamped", 'orange')
    plot_cubic_spline(xlist2, ylist2, len(xlist2) - 1, "clamped", 'green')
    plot_cubic_spline(xlist3, ylist3, len(xlist3) - 1, "clamped", 'red')

    plt.title('Cubic Spline Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    choice = input("Enter '1' to solve the example question or '2' for question 32: ")

    if choice == '1':
        n = int(input("Enter the value of n: "))
        spline_type = input("Press '1' for NATURAL or '2' for CLAMPED cubic spline: ")
        interval = [-2, 2]

        spline_type_str = "natural" if spline_type == '1' else "clamped"

        x, y = generate_data(n, interval)

        plt.figure(figsize=(10, 6))

        plt.scatter(x, y, color='black', label='Data Points', marker='o')
        plot_original_polynomial(interval, 'blue')

        plot_cubic_spline(x, y, n, spline_type_str, 'orange')

        plt.title('Cubic Spline Interpolation')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()

    elif choice == '2':
        solve_question_32()


if __name__ == "__main__":
    main()
