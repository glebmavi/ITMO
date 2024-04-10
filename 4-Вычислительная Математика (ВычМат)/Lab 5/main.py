# Title: Усовершенствованный метод Эйлера
#
# Реализуйте усовершенствованный метод Эйлера для решения обыкновенных дифференциальных уравнений по начальному значению (задача Коши) в интервале от a до b [a,b].
# f
# epsilon
# a
# y(a)
# b
# f - номер уравнения, где уравнение в виде y'=f(x,y). Вы должны получить функцию по номеру из входных данных в методе get_function.
# Вы должны определить и пересчитать шаг h самостоятельно.
# Вы должны вычислить и вернуть y(b) с разницей, не превышающей epsilon.

import math
import logging

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


class Result:

    @staticmethod
    def first_function(x: float, y: float):
        return math.sin(x)

    @staticmethod
    def second_function(x: float, y: float):
        return (x * y) / 2

    @staticmethod
    def third_function(x: float, y: float):
        return y - (2 * x) / y

    @staticmethod
    def fourth_function(x: float, y: float):
        return x + y

    @staticmethod
    def default_function(x: float, y: float):
        return 0.0

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
        else:
            return Result.default_function

    #
    # Complete the 'solveByEulerImproved' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. INTEGER f
    #  2. DOUBLE epsilon
    #  3. DOUBLE a
    #  4. DOUBLE y_a
    #  5. DOUBLE b
    #
    @staticmethod
    def solveByEulerImproved(f, epsilon, a, y_a, b):
        """
        Решает обыкновенное дифференциальное уравнение методом усовершенствованного Эйлера.

        :param f: Номер выбранной функции
        :param epsilon: Точность
        :param a: Нижняя граница интервала.
        :param y_a: Значение функции в точке a.
        :param b: Верхняя граница интервала.
        :return: Вычисленное значение функции в точке b.
        """
        func = Result.get_function(f)

        # Начальные условия
        x, y = a, y_a
        h = (b-a) * epsilon  # начальный шаг

        while x < b:
            # Вычисляем прогноз
            y_predict = y + h * func(x, y)

            # Вычисляем коррекцию
            y_correct = y + h * (func(x, y) + func(x + h, y_predict)) / 2

            # Проверяем, достаточно ли маленькая разница между прогнозом и коррекцией
            while abs(y_correct - y_predict) > epsilon:
                # Если разница слишком большая, уменьшаем шаг и повторяем процесс
                h /= 2
                y_predict = y + h * func(x, y)
                y_correct = y + h * (func(x, y) + func(x + h, y_predict)) / 2

            # Обновляем x и y
            x += h
            y = y_correct

        logging.debug(f"Step: {h}")
        return y


if __name__ == '__main__':
    f = int(input().strip())

    epsilon = float(input().strip())

    a = float(input().strip())

    y_a = float(input().strip())

    b = float(input().strip())

    result = Result.solveByEulerImproved(f, epsilon, a, y_a, b)

    print(str(result) + '\n')


"""
#1
1
1e-6
0
0
3.141592653589793

#2
2
1e-6
0
2
2

#3
3
1e-6
0
1
4

#4
4
1e-6
5
-5
6

#5
4
1e-6
0
10
5
"""