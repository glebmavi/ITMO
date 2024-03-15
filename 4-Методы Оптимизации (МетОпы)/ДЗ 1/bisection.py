# Поиск минимума функции методом деления отрезка пополам

def calculate_and_update(f, a, b, delta):
    x_1 = (b + a - delta) / 2
    x_2 = (b + a + delta) / 2
    f_1, f_2 = f(x_1), f(x_2)
    if f_1 <= f_2:
        b = x_2
    else:
        a = x_1
    return a, b


def bisection(f, a, b, delta, epsilon, max_steps=25):
    results = []
    i = 0
    print(f"i = {i}: a = {a}, b = {b}")

    for i in range(1, max_steps + 1):
        if abs(b - a) <= 2 * epsilon:
            break
        a, b = calculate_and_update(f, a, b, delta)
        print(f"i = {i}: a = {a}, b = {b}")
        results.append((a + b) / 2)
    return results

