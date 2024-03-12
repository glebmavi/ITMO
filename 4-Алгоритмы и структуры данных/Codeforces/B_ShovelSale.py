def shovel_sale(n):
    pairs = 0
    summ = n + (n - 1)
    if summ < 9:
        return n * (n - 1) // 2
    if set(str(summ)) <= {'9'}:
        return 1
    else:
        length = len(str(summ))
        cur = (length - 1) * '9'
        possible_summs = [int(f'{i}{cur}') for i in range(9) if int(f'{i}{cur}') <= summ]
        for p in possible_summs:
            if p <= n + 1:
                pairs += p//2
            else:
                pairs += (n - (p - n) + 1)//2
        return pairs


if __name__ == "__main__":
    print(shovel_sale(int(input())))
