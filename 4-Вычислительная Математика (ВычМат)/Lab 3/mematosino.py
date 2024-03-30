# Title: Метод простых итераций
#
# Дана система нелинейных уравнений. По заданному начальному приближению необходимо найти решение системы с точностью до 5 верного знака после запятой при помощи метода простых итераций.
#
# Формат входных данных:
# k
# n
# x0
# y0
# ...
#
# где k - номер системы, n - количество уравнений и количество неизвестных, а остальные значения - начальные приближения для соответствующих неизвестных.
#
# Формат выходных данных: список такого же типа данных, как списки входных данных, содержащие значения корня для каждой из неизвестных с точностью до 5 верного знака.


import math
import os
import random
import re
import sys
import logging

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


def first_function(args: []) -> float:
    return math.sin(args[0])


def second_function(args: []) -> float:
    return (args[0] * args[1]) / 2


def third_function(args: []) -> float:
    return (pow(args[0], 2) * pow(args[1], 2)) - (3 * pow(args[0], 3)) - (6 * pow(args[1], 3)) + 8


def fourth_function(args: []) -> float:
    return pow(args[0], 4) - 9 * args[1] + 2


def fifth_function(args: []) -> float:
    return args[0] + pow(args[0], 2) - 2 * args[1] * args[2] - 0.1


def six_function(args: []) -> float:
    return args[1] + pow(args[1], 2) + 3 * args[0] * args[2] + 0.2


def seven_function(args: []) -> float:
    return args[2] + pow(args[2], 2) + 2 * args[0] * args[1] - 0.3


def default_function(args: []) -> float:
    return 0.0


# How to use this function:
# funcs = Result.get_functions(4)
# funcs[0](0.01)
def get_functions(n: int):
    if n == 1:
        return [first_function, second_function]
    elif n == 2:
        return [third_function, fourth_function]
    elif n == 3:
        return [fifth_function, six_function, seven_function]
    else:
        return [default_function]


#
# Complete the 'solve_by_fixed_point_iterations' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER system_id
#  2. INTEGER number_of_unknowns
#  3. DOUBLE_ARRAY initial_approximations
#
def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
    epsilon = 5e-6
    max_iterations = 10000
    funcs = get_functions(system_id)
    current_approximations = initial_approximations.copy()
    next_approximations = [0.0] * number_of_unknowns
    parameter = [0.001] * number_of_unknowns # изменено, чтобы сделать метод более сходимым

    for _ in range(max_iterations):

        for i in range(number_of_unknowns):
            try:
                next_approximations[i] = current_approximations[i] - funcs[i](current_approximations) * parameter[i]
            except Exception as e:
                raise ValueError(
                    f"The initial approximations do not converge to a solution for the given system. Error: {e}")

        if all(abs(next_approximations[i] - current_approximations[i]) < epsilon for i in range(number_of_unknowns)):
            logging.debug(f"Converged after {_} iterations")
            logging.debug(f"Current parameters: {parameter}")
            logging.debug(f"Function values: {[func(current_approximations) for func in funcs]}")
            return next_approximations

        for i in range(number_of_unknowns):
            if abs(funcs[i](next_approximations)) >= abs(funcs[i](current_approximations)):
                parameter[i] = -parameter[i] # изменено, чтобы сделать метод более сходимым

        current_approximations = next_approximations.copy()

    raise ValueError("The method did not converge within the maximum number of iterations")


if __name__ == '__main__':
    system_id = int(input().strip())

    number_of_unknowns = int(input().strip())

    initial_approximations = []

    for _ in range(number_of_unknowns):
        initial_approximations_item = float(input().strip())
        initial_approximations.append(initial_approximations_item)

    result = solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations)

    print('\n'.join(map(str, result)))

"""
Tests:

1
2
0.2
0.5

1
2
300
210

2
2
-2
2

2
2
-1.9
2.1

2
2
1.5
0.5

3
3
-0.1
-0.5
0.2

3
3
-3
2
3

3
3
5
10
-5

"""
