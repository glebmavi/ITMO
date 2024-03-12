def run(query, n):
    p_count = query.count('+')
    m_count = query.count('-')

    min_sum = (p_count + 1) - n * m_count
    max_sum = n * (p_count + 1) - m_count

    if min_sum > n or max_sum < n:
        print("Impossible")
        return

    print("Possible")
    s = n
    min_left = s + p_count - n * m_count
    max_left = s + n * p_count - m_count
    while n < min_left or n > max_left:
        s -= 1
        min_left = s + p_count - n * m_count
        max_left = s + n * p_count - m_count
    query[0] = str(s)

    for i in range(p_count + m_count):
        x = 1
        sign = 1
        if query[2 * i + 1] == '-':
            sign = -1
            m_count -= 1
        elif query[2 * i + 1] == '+':
            sign = 1
            p_count -= 1
        min_left = s + sign * x + p_count - n * m_count
        max_left = s + sign * x + n * p_count - m_count
        while n < min_left or n > max_left:
            x += 1
            min_left = s + sign * x + p_count - n * m_count
            max_left = s + sign * x + n * p_count - m_count
        query[2 * i + 2] = str(x)
        s += sign * x
        if query[2 * i + 1] == '=':
            break

    equation = ' '.join(query)
    # solution = equation.split('=')[0]
    # res = eval(solution)
    # if res != n:
    #     raise ValueError("Incorrect solution")

    # print(equation + ": " + str(res))
    print(equation)


if __name__ == "__main__":
    # get input from console
    query = input().split()
    n = int(query[-1])
    run(query, n)

    # # get input from file CRebus.txt
    # with open("CRebus.txt", "r") as file:
    #     for _ in range(int(file.readline())):
    #         query = file.readline().split()
    #         n = int(query[-1])
    #         run(query, n)
