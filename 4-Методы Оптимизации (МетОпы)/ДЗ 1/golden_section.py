# Поиск минимума функции методом золотого сечения
import math


def golden_section(f, a, b, delta, max_steps=25):
    results = []
    tau = (math.sqrt(5) - 1) / 2
    i = 0
    print(f"i = {i}: a = {a}, b = {b}")
    x_1 = a + (1 - tau) * (b - a)
    x_2 = a + tau * (b - a)
    f_1, f_2 = f(x_1), f(x_2)

    for i in range(1, max_steps + 1):
        if abs(b - a) <= 2 * delta:
            break
        if f_1 <= f_2:
            b = x_2
            x_2, f_2 = x_1, f_1
            x_1 = b - (b - a) * tau
            f_1 = f(x_1)
        else:
            a = x_1
            x_1, f_1 = x_2, f_2
            x_2 = a + (b - a) * tau
            f_2 = f(x_2)

        print(f"i = {i}: a = {a}, b = {b}")
        results.append((a + b) / 2)

    return results
