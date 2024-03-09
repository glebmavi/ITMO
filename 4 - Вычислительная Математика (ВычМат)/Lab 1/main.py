# Дан набор точек, по которым необходимо построить интерполяционную функцию по методу кубических сплайнов с использованием полиномов Чебышёвадля заданного интервала. Также задана координата x, для которой необходимо найти значение интерполяционного полинома.
#
# Формат входных данных:
# f
# a
# b
# x
#
# где f - номер интерполируемой функции, a и b - границы интерполируемого интервала и x - значение аргумента для интерполяционного полинома.
#
# Степень полинома Чебышева (количество узлов интерполяции) следует увеличивать до тех пор, пока модуль разницы между значениями интерполирующей функции в искомой точке x не будет меньше чем 0.01.
#
# Формат выходных значений: вещественное число, являющееся значением интерполяционной функции в точке x.
import logging
import math
import os
import random
import re
import sys


logging.basicConfig(format='%(message)s', level=logging.DEBUG)

class FunctionSet:

    def weierstrass_function(x: float):
        f_x = 0.0
        n = 5
        b = 0.5
        a = 13
        for i in range(n):
            f_x += pow(b, i) * math.cos(pow(a, n) * math.pi * x)

        return f_x

    def gamma_function(x: float):
        # made for consistency with other languages. Normally math.gamma can be used.
        tmp = (x - 0.5) * math.log(x + 4.5) - (x + 4.5)
        ser = 1.0 + 76.18009173 / (x + 0.0) - 86.50532033 / (x + 1.0) + 24.01409822 / (x + 2.0) - 1.231739516 / (
                x + 3.0) + 0.00120858003 / (x + 4.0) - 0.00000536382 / (x + 5.0)

        return math.exp(tmp + math.log(ser * math.sqrt(2 * math.pi)))

    # only for testing purposes:
    def square_function(x: float):
        return x * x

    # How to use this function:
    # func = FunctionSet.get_function(4)
    # func(0.01)
    def get_function(n: int):
        if n == 1:
            return FunctionSet.weierstrass_function
        elif n == 2:
            return FunctionSet.gamma_function
        elif n == 3:
            return FunctionSet.square_function
        else:
            raise NotImplementedError(f"Function {n} not defined.")


def cubic_spline_interpolation(x_values, y_values, x):
    """
    Находит значение интерполяционного многочлена в точке x с помощью натурального кубического сплайна


    На каждом отрезке [x[i], x[i+1]] интерполяционный многочлен имеет вид:

    S[i](x) = a[i] + b[i](x - x[i]) + c[i](x - x[i])^2 + d[i](x - x[i])^3,

    где a[i], b[i], c[i], d[i] - неизвестные коэффициенты


    Производные интерполяционного многочлена в узлах интерполяции:

    S[i](x[i]) = a[i]; S[i]'(x[i]) = b[i]; S[i]''(x[i]) = 2c[i]; S[i]'''(x[i]) = 6d[i],

    для всех i = 1, 2, ..., n


    Условия непрерывности первой и второй производных интерполяционного многочлена в узлах интерполяции:

    S[i](x[i-1]) = S[i-1](x[i-1]) для всех i = 2, 3, ..., n

    S[i]'(x[i-1]) = S[i-1]'(x[i-1]) для всех i = 2, 3, ..., n

    S[i]''(x[i-1]) = S[i-1]''(x[i-1]) для всех i = 2, 3, ..., n

    :param x_values: Узлы интерполяции
    :param y_values: Значения функции в узлах интерполяции
    :param x: Точка, в которой необходимо найти значение интерполяционного многочлена
    :return: Значение интерполяционного многочлена в точке x
    """

    # Количество узлов интерполяции
    n = len(x_values)
    # Коэффициенты интерполяционного многочлена a равны значениям функции в узлах интерполяции
    a = y_values.copy()
    # Коэффициенты интерполяционного многочлена b, c, d, которые необходимо найти
    b = [0] * n
    c = [0] * n
    d = [0] * n

    # h - длины отрезков [x[i], x[i+1]]
    h = [x_values[i] - x_values[i - 1] for i in range(1, n)]

    # alpha - коэффициенты для прогоночного метода
    alpha = [3 * (a[i] - a[i - 1]) / h[i - 1] - 3 * (a[i - 1] - a[i - 2]) / h[i - 2] for i in range(2, n)]
    alpha.insert(0, 3 * (a[1] - a[0]) / h[0])

    # l, mu, z - Коэффициенты для прогоночного метода
    l = [1] + [0] * (n - 1)
    mu = [0] * n
    z = [0] * n

    # Решение прогоночной системы для коэффициентов c
    for i in range(1, n - 1):
        l[i] = 2 * (x_values[i + 1] - x_values[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    # Установка граничных условий для второй производной равной нулю в начале и в конце отрезка
    l[n - 1] = 1
    z[n - 1] = 0
    c[n - 1] = 0

    # Находим коэффициенты c, b, d
    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (a[j + 1] - a[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # Находим значение интерполяционного многочлена в точке x если x принадлежит отрезку [x[i], x[i+1]]
    for i in range(n - 1):
        if x_values[i] <= x <= x_values[i + 1]:
            delta_x = x - x_values[i]
            return a[i] + b[i] * delta_x + c[i] * delta_x ** 2 + d[i] * delta_x ** 3
    raise ValueError("x is not in the interval of interpolation nodes")


def chebyshev_nodes(a, b, n):
    """
    Возвращает узлы интерполяции - корни полиномов Чебышева
    :param a: Начало интервала
    :param b: Конец интервала
    :param n: Количество узлов интерполяции (степень полинома Чебышева)
    :return: Список узлов интерполяции
    """
    return [(a + b) / 2 + (b - a) / 2 * math.cos(((2 * k - 1) / n) * (math.pi / 2)) for k in range(n, 0, -1)]


#
# Complete the 'interpolate_by_spline' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. INTEGER f
#  2. DOUBLE a
#  3. DOUBLE b
#  4. DOUBLE x
#
def interpolate_by_spline(f, a, b, x):
    """
    Интерполяция кубическими сплайнами

    :param f: Номер интерполируемой функции
    :param a: Начало интервала для значения x
    :param b: Конец интервала для значения x
    :param x: Значение аргумента для интерполяционного полинома
    :return: Значение интерполяционного полинома в точке x
    """

    # Функция, которую необходимо интерполировать
    try:
        function = FunctionSet.get_function(f)
    except NotImplementedError:
        print(f"Function {f} not defined.")
        return

    # Ожидаемое значение интерполяционного многочлена в точке x
    expected_value = function(x)
    logging.debug(f"Expected y value: {expected_value}")

    # Узлы интерполяции
    if a > b:
        print("Invalid interval")
        return
    degree = int((b - a) // min(abs(a - x), abs(b - x)))
    logging.debug(f"Initial degree: {degree}")
    x_values = chebyshev_nodes(a, b, degree)

    # Значения функции в узлах интерполяции
    y_values = [function(x) for x in x_values]

    # Находим значение интерполяционного многочлена в точке x
    try:
        res = cubic_spline_interpolation(x_values, y_values, x)
    except ValueError:
        print("x is not in the interval of interpolation nodes")
        return

    logging.debug(f"First time interpolated y value: {res}")

    # Увеличиваем количество узлов интерполяции, пока модуль разницы между значениями интерполирующей функции в
    # искомой точке x, не будет меньше чем 0.01 и повторяем интерполяцию
    counter = 0
    while abs(res - expected_value) > 0.01:
        if counter > 1000:
            raise ValueError("Too many iterations")
        degree += 1
        x_values = chebyshev_nodes(a, b, degree)
        y_values = [function(x) for x in x_values]
        res = cubic_spline_interpolation(x_values, y_values, x)
        counter += 1
    logging.debug(f"Final interpolated y value: {res}")
    logging.debug(f"Relative error: {abs(res - expected_value)/expected_value * 100}%")
    logging.debug(f"Final degree: {degree}")
    logging.debug(f"Number of iterations: {counter}")
    return res


if __name__ == '__main__':
    f = 1
    a = -1
    b = 1
    x = 0

    # f = int(input().strip())
    # a = float(input().strip())
    # b = float(input().strip())
    # x = float(input().strip())

    result = interpolate_by_spline(f, a, b, x)

    print(str(result) + '\n')
