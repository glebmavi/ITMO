# Поиск минимума функции методом Ньютона

def newton(f_prime, f_double_prime, x, epsilon, max_steps=25):
    results = []
    i = 0
    print(f"i = {i}: x = {x}")

    for i in range(1, max_steps + 1):
        if abs(f_prime(x)) <= epsilon:
            break
        x = x - f_prime(x) / f_double_prime(x)
        print(f"i = {i}: x = {x}")
        results.append(x)

    return results
