import random


def create_matrix(m, n, k):
    matrix1 = [[random.randint(-9, 9) for x in range(m)] for _ in range(k)]
    matrix2 = [[random.randint(-9, 9) for x in range(k)] for _ in range(n)]
    return matrix1, matrix2


def print_matrix(matrix1, matrix2):
    print("Созданная матрица 1:")
    for i in matrix1:
        print(i)
    print("Созданная матрица 2:")
    for i in matrix2:
        print(i)


def choose_mode(n, m1, m2):
    if n == 1:
        print_matrix(m1, m2)
        matrix_addition(m1, m2)
    elif n == 2:
        print_matrix(m1, m2)
        matrix_subtraction(m1, m2)
    elif n == 3:
        print_matrix(m1, m2)
        matrix_multiplication(m1, m2)
    elif n == 4:
        print_matrix(m1, m2)
        print("Результат транспонирования первой матрицы:")
        transpose_matrix(m1)
        print("Результат транспонирования второй матрицы:")
        transpose_matrix(m2)
    elif n == 5:
        print_matrix(m1, m2)
        print("Определитель первой матрицы:")
        determinant(m1)
        print("Определитель второй матрицы:")
        determinant(m2)
    elif n == 6:
        print_matrix(m1, m2)
        print("Обратная матрица к первой матрице:")
        inverse_matrix(m1)
        print("Обратная матрица ко второй матрице:")
        inverse_matrix(m2)


def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Невозможно сложить матрицы разного размера.")
    else:
        rows = len(matrix1)
        cols = len(matrix1[0])
        result = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        print("Результат сложения матриц:")
        for elem in result:
            print(elem)


def matrix_subtraction(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Невозможно вычесть матрицы разного размера.")
    else:
        rows = len(matrix1)
        cols = len(matrix1[0])
        result = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrix1[i][j] - matrix2[i][j]
        print("Результат вычитания матриц:")
        for elem in result:
            print(elem)


def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print(f"Количество столбцов первой матрицы ({len(matrix1[0])}) должно равняться количеству строк второй "
              f"матрицы ({len(matrix2)})")
    else:
        m = len(matrix1)
        n = len(matrix1[0])
        p = len(matrix2[0])
        result = [[0 for _ in range(p)] for _ in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        print("Результат умножения матриц:")
        for elem in result:
            print(elem)


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    for elem in result:
        print(elem)


def determinant(matrix):
    n = len(matrix)
    if n == 0 or len(matrix[0]) != n:
        print("Невозможно найти определитель. Матрица должна быть квадратной")
    else:
        if n == 1:
            print(matrix[0][0])
        elif n == 2:
            print(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
        elif n == 3:
            print(matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
                  matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
                  matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
        else:
            det = 0
            for j in range(n):
                minor = []
                for i in range(1, n):
                    row = []
                    for k in range(n):
                        if k != j:
                            row.append(matrix[i][k])
                    minor.append(row)

                minor_det = determinant(minor)
                det += (-1) ** j * matrix[0][j] * minor_det

            return det


def inverse_matrix(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            print("Матрица должна быть квадратной")
        else:

            A = [row[:] for row in matrix]
            augmented = []
            for i in range(n):
                row = A[i][:]
                row.extend([1 if j == i else 0 for j in range(n)])
                augmented.append(row)

            # Прямой ход метода Гаусса
            for i in range(n):
                pivot_row = i
                for j in range(i + 1, n):
                    if abs(augmented[j][i]) > abs(augmented[pivot_row][i]):
                        pivot_row = j

                if abs(augmented[pivot_row][i]) < 1e-10:
                    print("Матрица вырожденная")

                if pivot_row != i:
                    augmented[i], augmented[pivot_row] = augmented[pivot_row], augmented[i]

                pivot = augmented[i][i]
                for j in range(2 * n):
                    augmented[i][j] = augmented[i][j] / pivot

                for j in range(n):
                    if j != i:
                        factor = augmented[j][i]
                        for k in range(2 * n):
                            augmented[j][k] = augmented[j][k] - factor * augmented[i][k]

            inverse = []
            for i in range(n):
                inverse.append(augmented[i][n:])

            for elem in inverse:
                print(elem)


def main():
    while True:
        try:
            m = int(input("Введите значение M: "))
            n = int(input("Введите значение N: "))
            k = int(input("Введите значение K: "))
            if m > 0 and n > 0 and k > 0:
                break
            else:
                print("Ошибка. Значения должны быть положительными. Попробуйте снова.")
        except ValueError:
            print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")
    while True:
        try:
            mode = int(input("Выберите действие с матрицами:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. "
                             "Транспонирование\n5. Определитель\n6. Обратная матрица\nВаш выбор (1-6): "))
            if 1 <= mode <= 6:
                break
            else:
                print("Ошибка. Введите число от 1 до 4.")
        except ValueError:
            print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")
    choose_mode(mode, *create_matrix(m, n, k))


main()
