import logging, atexit

logging.basicConfig(format='%(message)s', level=logging.DEBUG)


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        return res

    def print_count():
        print(f"{func.__name__}: {wrapper.count} times")

    atexit.register(print_count)
    wrapper.count = 0
    return wrapper


@count_calls
def is_diagonally_dominant(matrix):
    """
    Проверяет, имеет ли матрица диагональное преобладание и хотя бы одна строка имеет строго диагональное преобладание.
    :param matrix: 2D список, представляющий коэффициентную матрицу, дополненную вектором правой части.
    :return: True, если матрица имеет диагональное преобладание, False в противном случае.
    """
    found_strictly_dominant = False
    for i in range(n):
        if get_number_dominance_in_list(matrix[i], i) == "Not dominant":
            return False
        elif get_number_dominance_in_list(matrix[i], i) == "Strictly dominant":
            found_strictly_dominant = True
    return found_strictly_dominant


@count_calls
def get_number_dominance_in_list(row, index):
    """
    Проверяет, является ли число в данном индексе доминирующим в данной строке. Игнорируется последнее число.
    :param row: 1D список, представляющий строку в матрице.
    :param index: Индекс числа для проверки.
    :return: "Strictly dominant", если число строго доминирует, "Weakly dominant", если число слабо доминирует,
    "Not dominant" в противном случае.
    """
    value = abs(row[index])
    sum_of_other_values = sum(abs(row[i]) for i in range(n) if i != index)
    if value > sum_of_other_values:
        return "Strictly dominant"
    elif value == sum_of_other_values:
        return "Weakly dominant"
    else:
        return "Not dominant"


@count_calls
def swap_rows(matrix, row1, row2):
    """
    Обменивает две строки матрицы.
    :param matrix: 2D список, представляющий матрицу.
    :param row1: Индекс первой строки для обмена.
    :param row2: Индекс второй строки для обмена.
    :return: Матрица с обмененными строками.
    """
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    return matrix


@count_calls
def swap_columns(matrix, col1, col2):
    """
    Обменивает два столбца матрицы, исключая последний столбец.
    :param matrix: 2D список, представляющий матрицу.
    :param col1: Индекс первого столбца для обмена.
    :param col2: Индекс второго столбца для обмена.
    :return: Матрица с обмененными столбцами.
    """
    for i in range(n):
        if col1 != n and col2 != n:
            matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
    return matrix


def gauss_seidel(matrix, epsilon):
    """
    Выполняет итерацию Гаусса-Зейделя для решения системы линейных уравнений.
    :param matrix: 2D список, представляющий коэффициентную матрицу, дополненную вектором правой части.
    :param epsilon: Желаемая точность.
    :return: Вектор решения.
    """
    x = [0] * n  # Вектор начального приближения
    converge = False
    iterations = 0

    while not converge:
        x_copy = x[:]

        for i in range(n):
            s1 = sum(matrix[i][j] * x_copy[j] for j in range(i))
            s2 = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
            x_copy[i] = (matrix[i][-1] - s1 - s2) / matrix[i][i]

        # Проверка сходимости
        converge = all(abs(x_copy[i] - x[i]) < epsilon for i in range(n))
        x = x_copy
        iterations += 1

    return x, iterations


class Result:
    isMethodApplicable = True
    errorMessage = ""

    @staticmethod
    def solveByGaussSeidel(n, matrix, epsilon):
        """
        Решает систему линейных уравнений с использованием метода Гаусса-Зейделя.
        :param n: Количество уравнений.
        :param matrix: 2D список, представляющий коэффициентную матрицу, дополненную вектором правой части.
        :param epsilon: Желаемая точность.
        :return: Вектор решения, если успешно, пустой список в противном случае.
        """

        # Индексы переменных
        var_indices = [i for i in range(n)]

        if not is_diagonally_dominant(matrix):
            # Произвести перестановку строк и столбцов, чтобы достичь диагонального преобладания
            for i in range(n):
                if get_number_dominance_in_list(matrix[i], i) == "Not dominant":
                    # Искать строку, в которой число доминирующее
                    for j in range(i + 1, n):
                        if get_number_dominance_in_list(matrix[j], i) != "Not dominant":
                            matrix = swap_rows(matrix, i, j)
                            break
            if not is_diagonally_dominant(matrix):
                # Изменение столбцов, если изменение строк не помогло
                for i in range(n):
                    if get_number_dominance_in_list([matrix[j][i] for j in range(n)], i) == "Not dominant":
                        for j in range(i + 1, n):
                            if get_number_dominance_in_list([matrix[k][j] for k in range(n)], i) != "Not dominant":
                                matrix = swap_columns(matrix, i, j)
                                # Сохранить новый порядок переменных
                                var_indices[i], var_indices[j] = var_indices[j], var_indices[i]
                                break
        if any(matrix[i][i] == 0 for i in range(n)) or not is_diagonally_dominant(matrix):
            # Система не может иметь диагонального преобладания, метод Гаусса-Зейделя не применим
            Result.isMethodApplicable = False
            Result.errorMessage = ("The system has no diagonal dominance for this method. Method of the "
                                   "Gauss-Seidel is not applicable.")
            return []

        x, iterations = gauss_seidel(matrix, epsilon)
        # Восстановление исходного порядка переменных, если он был изменен
        x = [x[i] for i in var_indices]
        logging.debug(f"Iterations: {iterations}")
        return x


if __name__ == '__main__':
    n = int(input().strip())

    matrix_rows = n
    matrix_columns = n + 1

    matrix = []

    for _ in range(matrix_rows):
        matrix.append(list(map(float, input().rstrip().split())))

    epsilon = float(input().strip())

    result = Result.solveByGaussSeidel(n, matrix, epsilon)
    if Result.isMethodApplicable:
        print('\n'.join(map(str, result)))
    else:
        print(f"{Result.errorMessage}")

