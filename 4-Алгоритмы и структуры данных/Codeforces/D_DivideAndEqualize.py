from collections import Counter
from math import sqrt


def get_primes(n):
    primes = []
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            primes.append(i)
            n = n // i
    if n > 1:
        primes.append(n)
    return primes


def divide_and_equalize(n, a):
    if all(x == a[0] for x in a):
        print("yes")
        return
    else:
        frequency = Counter()
        for i in range(n):
            if a[i] != 1:
                primes = get_primes(a[i])
                frequency.update(primes)

        for value in frequency.values():
            if value % n != 0:
                print("no")
                return

        print("yes")
        return


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        divide_and_equalize(n, a)
