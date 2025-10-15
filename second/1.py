from math import *


def solve_circle(radius):
    perimeter = 2 * pi * radius
    area = pi * radius ** 2
    print("Периметр круга:", perimeter)
    print("Площадь круга:", area)


def find_perimeter(coordinates):
    if coordinates:
        p = 0
        n = len(coordinates)
        for i in range(n):
            p += distance(coordinates[i], coordinates[(i + 1) % n])
        return p
    else:
        return 0


def find_polygon_area(coordinates):
    area = 0
    n = len(coordinates)
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2


def distance(coordinate1, coordinate2):
    return ((coordinate1[0] - coordinate2[0]) ** 2 + (coordinate1[1] - coordinate2[1]) ** 2) ** 0.5


def solver(coordinates):
    if len(coordinates) == 3:
        print("Площадь треугольника:", find_triangle_area(*coordinates))
        print("Периметр треугольника:", round(find_perimeter(coordinates), 2))
    elif len(coordinates) >= 4:
        print("Площадь многоугольника:", find_polygon_area(coordinates))
        print("Периметр многоугольника:", find_perimeter(coordinates))
    else:
        print("Введите больше координат вершин для определения фигуры")


def find_triangle_area(p1, p2, p3):
    return 0.5 * abs((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]))


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
