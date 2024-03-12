def reader():
    return input(), input()


def precompute_powers(x, p, n):
    powers = [1] * (n + 1)
    for i in range(1, n + 1):
        powers[i] = (powers[i - 1] * x) % p
    return powers


def compute_hash(text, size, x, p):
    hash_value = 0
    for i in range(size):
        hash_value = (hash_value * x + ord(text[i])) % p
    return hash_value


def rabin_karp(pattern, text):
    m, n = len(pattern), len(text)
    x = 53
    p = 500009
    powers = precompute_powers(x, p, n)
    hash_values = [0] * (n - m + 1)

    # precompute hash values
    current_hash = compute_hash(text, m, x, p)
    hash_values[0] = current_hash

    # compute hash values
    for i in range(1, n - m + 1):
        current_hash = (current_hash - ord(text[i - 1]) * powers[m - 1]) % p  # remove the first character
        current_hash = (current_hash * x + ord(text[i + m - 1])) % p  # add the next character
        hash_values[i] = current_hash

    # compute pattern hash
    pattern_hash = compute_hash(pattern, m, x, p)

    # find matches
    result = []
    for i in range(n - m + 1):
        if pattern_hash != hash_values[i]:
            continue
        if text[i:i + m] == pattern:
            result.append(i)

    return result


if __name__ == '__main__':
    pattern, text = reader()
    print(*rabin_karp(pattern, text))
