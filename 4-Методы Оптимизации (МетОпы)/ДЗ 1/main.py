import math
import matplotlib.pyplot as plt
import numpy as np
import bisection, golden_section, newton


def f(x):
    return (1 / 3) * x ** 3 - 5 * x + x * math.log(x)


def f_prime(x):
    return x ** 2 - 4 + math.log(x)


def f_double_prime(x):
    return 2 * x + (1 / x)


def plot_results(f, a, b, results=None, color=None, title=None):
    x_values = np.linspace(a, b, 100)
    y_values = [f(x) for x in x_values]

    plt.plot(x_values, y_values)
    if results and color:
        plt.plot(results, [f(res) for res in results], color)
        plt.axvline(x=results[-1], color=color[0])

    plt.title(title if title else '')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    a = 1.5
    b = 2
    epsilon = 10 ** -10
    delta = epsilon

    plot_results(f, a, b, None, None, "Исходная функция")

    # Метод половинного деления
    print("Метод половинного деления")
    result = bisection.bisection(f, a, b, delta, epsilon)
    print("Найденный минимум: ", result[-1], "\n")
    plot_results(f, a, b, result, 'bo', "Метод половинного деления")

    # Метод золотого сечения
    print("Метод золотого сечения")
    result = golden_section.golden_section(f, a, b, epsilon)
    print("Найденный минимум: ", result[-1], "\n")
    plot_results(f, a, b, result, 'go', "Метод золотого сечения")

    # Метод Ньютона
    print("Метод Ньютона")
    result = newton.newton(f_prime, f_double_prime, (a + b) / 2, epsilon)
    print("Найденный минимум: ", result[-1], "\n")
    plot_results(f, a, b, result, 'ro', "Метод Ньютона")
