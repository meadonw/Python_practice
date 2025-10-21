import math


def solve_circle(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print("Периметр круга:", perimeter)
    print("Площадь круга:", area)


def find_perimeter(coordinates):
    n = len(coordinates)
    perimeter = 0
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]
        perimeter += math.hypot(x2 - x1, y2 - y1)

    return perimeter


def find_area(coordinates):
    n = len(coordinates)
    area = 0
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]
        area += x1 * y2 - x2 * y1

    return abs(area) / 2


def solver(coordinates):
    if len(coordinates) == 3:
        print("Площадь треугольника:", find_area(coordinates))
        print("Периметр треугольника:", find_perimeter(coordinates))
    elif len(coordinates) >= 4:
        print("Площадь многоугольника:", find_area(coordinates))
        print("Периметр многоугольника:", find_perimeter(coordinates))
    else:
        print("Многоугольник должен иметь как минимум 3 вершины")


def main():
    while True:
        try:
            n = int(input("Введите кол-во вершин: "))
            if n >= 1:
                break
            else:
                print("Число должно быть положительным.")
        except ValueError:
            print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")
    if n == 1:
        while True:
            try:
                radius = float(input("Введите радиус круга: "))
                if radius > 0:
                    solve_circle(radius)
                    break
                else:
                    print("Радиус должен быть положительным.")
            except ValueError:
                print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")
    else:
        coordinates = []
        for i in range(n):
            while True:
                try:
                    x, y = map(float, input(f"Введите координаты {i + 1} точки: ").split())
                    coordinates.append([x, y])
                    break
                except ValueError:
                    print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")
        solver(coordinates)


main()
