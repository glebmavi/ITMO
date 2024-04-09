# Title: Метод средних прямоугольников
#
#
# Реализуйте метод средних прямоугольников для вычисления интеграла от выбранной функции на интервале от a до b.
# • Если функция имеет разрыв второго рода или "скачок", или если функция не определена какой-либо частью в интервале от a до b,
# то вам следует указать переменные error_message и hasDiscontinuity.
# • Сообщение об ошибке, которое вы должны указать: "Integrated function has discontinuity or does not defined in current interval".
# • Если функция имеет устранимый разрыв первого рода, то вы должны уметь вычислить интеграл.
# • Если a > b, то интеграл должен иметь отрицательное значение.
# Формат ввода:
# a
# b
# f
# epsilon
# , где a и b - границы интеграла,
# f - номер функции,
# epsilon - максимальная разница между двумя вашими итерациями
# (итерация - это некоторое разбиение на отрезки).
# Формат вывода:
# I
# , где I - ваш вычисленный интеграл для текущего количества разбиений.


import math
import os
import random
import re
import sys
import logging

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


class Result:
    error_message = ""
    has_discontinuity = False
    eps = 0

    @staticmethod
    def first_function(x: float):
        return 1 / x

    @staticmethod
    def second_function(x: float):
        if x == 0:
            return (math.sin(Result.eps) / Result.eps + math.sin(-Result.eps) / -Result.eps) / 2
        return math.sin(x) / x

    @staticmethod
    def third_function(x: float):
        return x * x + 2

    @staticmethod
    def fourth_function(x: float):
        return 2 * x + 2

    @staticmethod
    def five_function(x: float):
        return math.log(x)

    # How to use this function:
    # func = Result.get_function(4)
    # func(0.01)
    @staticmethod
    def get_function(n: int):
        if n == 1:
            return Result.first_function
        elif n == 2:
            return Result.second_function
        elif n == 3:
            return Result.third_function
        elif n == 4:
            return Result.fourth_function
        elif n == 5:
            return Result.five_function
        else:
            raise NotImplementedError(f"Function {n} not defined.")

    @staticmethod
    def has_function_discontinuity(f, a: float, b: float) -> bool:
        """
        Проверяет, имеет ли выбранная функция разрыв в интервале [a, b].
        :param f: Выбранная функция.
        :param a: Нижняя граница интервала.
        :param b: Верхняя граница интервала.
        :return: True, если функция имеет разрыв в интервале [a, b], иначе False.
        """
        try:
            if a <= 0 <= b:
                f(0)
            if a < 0 or b < 0:
                f(-1)
            f(a)
            f(b)
        except Exception:
            Result.has_discontinuity = True
            Result.error_message = "Integrated function has discontinuity or does not defined in current interval"
            return True

    @staticmethod
    def calculate_integral(a: float, b: float, f: int, epsilon: float) -> float:
        """
        Вычисляет интеграл выбранной функции на интервале [a, b] с использованием метода средних прямоугольников.
        :param a: Нижняя граница интервала.
        :param b: Верхняя граница интервала.
        :param f: Номер выбранной функции.
        :param epsilon: Максимальная разница между двумя итерациями.
        :return: Вычисленный интеграл для текущего количества разбиений.
        """
        Result.eps = epsilon
        func = Result.get_function(f)
        if Result.has_function_discontinuity(func, a, b):
            return 0.0

        n = 2  # Initial number of partitions
        prev_integral = 0.0
        integral = 0.0
        multiplier = 1

        if a > b:
            a, b = b, a
            multiplier = -1

        while True:
            h = (b - a) / n
            integral_sum = 0.0

            for i in range(n):
                xi = a + (i + 0.5) * h
                integral_sum += func(xi)

            integral = h * integral_sum

            if abs(integral - prev_integral) < epsilon:
                break

            prev_integral = integral
            n *= 2
        logging.debug(f"Interval width: {h}")
        logging.debug(f"Number of partitions: {n}")
        return integral * multiplier


if __name__ == '__main__':
    a = float(input().strip())

    b = float(input().strip())

    f = int(input().strip())

    epsilon = float(input().strip())

    result = Result.calculate_integral(a, b, f, epsilon)
    if not Result.has_discontinuity:
        print(str(result) + '\n')
    else:
        print(Result.error_message + '\n')

    print()

"""
Tests:

#1
0.1
3
1
1e-6

#2
0
4
1
1e-6

#3
-1
3
1
1e-10

#4
0
0
2
1e-6

#5
-6.7
-2.3
2
1e-6

#6
6
-6
2
1e-6

#7
123
456
3
1e-6

#8
-30
-50
4
1e-6


#9
0.1
3
5
1e-6

#10
0
-4
5
1e-6

#11
-1
1
5
1e-6
"""
