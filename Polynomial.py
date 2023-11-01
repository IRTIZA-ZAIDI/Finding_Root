import numpy as np
import matplotlib.pyplot as plt
import math

# evaluates Lagrange at x
def Lagrange(x):
    y = 0
    for i in range(len(x_values)):
        denominator = 1
        numerator = 1
        for j in range(len(y_values)):
            if i == j:
                continue
            numerator = numerator * (x - x_values[j])
            denominator = denominator * (x_values[i] - x_values[j])
        y = y + (numerator / denominator) * y_values[i]
    return y

# evaluates coefficients of Polynomial
def DDTable():
    DDTable = [y_values]
    for i in range(len(y_values) - 1):
        M = []
        for j in range(len(y_values) - 1 - i):
            numerator = DDTable[i][j + 1] - DDTable[i][j]
            denominator = x_values[j + 1 + i] - x_values[j]
            M.append(numerator / denominator)
        DDTable.append(M)
    return DDTable

# evaluates Polynomial at x
def DDPolynomial(x):
    y = DDTableArray[0][0]
    for i in range(len(y_values) - 1):
        P = 1
        for j in range(i + 1):
            P = P * (x - x_values[j])
        y = y + P * DDTableArray[i + 1][0]
    return y

# Given equation
def f(x):
    fx = "math.exp(x) + math.pow(2,-x) + 2*math.cos(x) - 6"
    val = eval(fx)
    return val


def generateGivenEquation():  # for given eq

    global x_values, y_values, LagrangeTable, DDTableArray, PolynomialTable, x_values_100, ErrorTableLagrange, ErrorTablePolynomial

    n = int(input("Enter value for n: "))
    x_values = np.linspace(-2, 2, n)
    y_values = []
    LagrangeTable = []
    DDTableArray = []
    PolynomialTable = []
    x_values_100 = np.linspace(-2, 2, 100)
    y_values_100 = []
    ErrorTableLagrange = []
    ErrorTablePolynomial = []

    for x in x_values:
        y_values.append(f(x))

    for x in x_values_100:
        y_values_100.append(f(x))

    for x in x_values_100:
        LagrangeTable.append(Lagrange(x))

    DDTableArray = DDTable()
    for x in x_values_100:
        PolynomialTable.append(DDPolynomial(x))


    for x in range(len(LagrangeTable)):
        ErrorTableLagrange.append(abs(float(y_values_100[x]) - LagrangeTable[x]))

    for x in range(len(PolynomialTable)):
        ErrorTablePolynomial.append(abs(float(y_values_100[x]) - PolynomialTable[x]))

    print("x_values: ", x_values)
    print("y_values: ", y_values)
    print("Lagrange coefficients: ", LagrangeTable, "\n")
    print("DD Polynomial coefficients: ", PolynomialTable, "\n")
    print("Lagrange Error: ", ErrorTableLagrange, "\n")
    print("Polynomial Error: ", ErrorTablePolynomial, "\n")
    print("DD Table: ")
    DDTablePrint()
    plt.subplot(2, 1, 1)
    plt.plot(x_values, y_values, label="f(x) n=" + str(len(y_values)), color='Green')
    plt.plot(x_values_100, LagrangeTable, label="Lagrange n=" + str(len(x_values_100)), color='Blue')
    plt.plot(x_values_100, PolynomialTable, label="Divided Difference n=" + str(len(x_values_100)), color='Red')
    plt.title("Given equation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.plot(x_values_100, ErrorTableLagrange, label="Lagrange n=" + str(len(x_values_100)), color='Blue')
    plt.plot(x_values_100, ErrorTablePolynomial, label="Divided Difference n=" + str(len(x_values_100)), color='Red')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.tight_layout()
    plt.savefig('eq.png')
    plt.show()


def ExampleQuestion_19():  # for q19

    global x_values
    global y_values
    global LagrangeTable

    global x_values_n

    x_values = [0, 6, 10, 13, 17, 20, 28]
    y_values = [6.67, 17.33, 42.67, 37.33, 30.10, 29.31, 28.74]
    LagrangeTable = []
    x_values_n = np.linspace(0, 28, 28)

    for x in x_values_n:
        LagrangeTable.append(Lagrange(x))  # values of Lagrange with n=28

    print("Instance 1")
    print("X: ", x_values)
    print("Y: ", y_values)
    print("Lagrange coefficients: ", LagrangeTable)
    print()
    print("Maximum Interpolated Weight: ", max(LagrangeTable))
    print()

    plt.clf()
    plt.plot(x_values, y_values, label="f(x) n=" + str(len(y_values)), color='Red')
    plt.plot(x_values_n, LagrangeTable, label="Lagrange n=" + str(len(x_values_n)), color='Blue')
    plt.title("Instance 1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig("Instance 1")
    plt.show()

    y_values = [6.67, 16.11, 18.89, 15.00, 10.56, 9.44, 8.89]
    LagrangeTable = []

    for x in x_values_n:
        LagrangeTable.append(Lagrange(x))  # values of Lagrange with n=28

    print("Instance 2")
    print("X: ", x_values)
    print("Y: ", y_values)
    print("Lagrange coefficients: ", LagrangeTable)
    print()
    print("Maximum Interpolated Weight: ", max(LagrangeTable))
    print()

    plt.clf()
    plt.plot(x_values, y_values, label="f(x) n=" + str(len(y_values)), color='Red')
    plt.plot(x_values_n, LagrangeTable, label="Lagrange n=" + str(len(x_values_n)), color='Blue')
    plt.title("Instance 2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig("Instance 2")
    plt.show()

# Print DDTable in triangle shape
def DDTablePrint():
    PrintTable = []
    max_num_length = 0;

    max_size = len(DDTableArray[0])
    for Diff in DDTableArray:

        size = max_size - len(Diff)
        newArr = []
        for num in Diff:
            num = '{:.4e}'.format(num)
            newArr.append(num)
            newArr.append(" ")
            max_num_length = max(max_num_length, len(str(num)))


        newArr = [" "] * size + newArr + [" "] * (size - 1)
        PrintTable.append(newArr)

    PrintTable[0].pop()


    PrintTable = np.transpose(PrintTable)

    for arr in PrintTable:
        for num in arr:
            print(num, end=" " * ((max_num_length + 1) - len(num)))
        print("", end="\n")


def main():
    decision = (input("Press (1) to interpolate given equation in the question\n"
                      "Press (2) to interpolate question 19 of Ex 3.1\n"))
    if decision == "1":
        generateGivenEquation()
        return
    elif decision == "2":
        ExampleQuestion_19()
        return
    else:
        print("This is not a valid option.")
        return

if __name__ == "__main__":
    main()