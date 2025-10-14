from math import *


def solve_circle(radius):
    perimeter = 2 * pi * radius
    area = pi * radius ** 2
    print("Периметр круга:", perimeter)
    print("Площадь круга:", area)


def find_area():
    pass


def main():
    while True:
        try:
            n = int(input("Введите кол-во вершин: "))
            if n == 1 or n > 2:
                break
            else:
                print("Число должно быть положительным.")
        except ValueError:
            print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")
    if n == 1:
        while True:
            try:
                radius = int(input("Введите радиус круга: "))
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
            try:
                x, y = map(float, input(f"Введите координаты {i + 1} точки").split())

            except ValueError:
                print("bad")


main()
