while True:
    try:
        a = float(input())
        b = float(input())
        c = float(input())
        if a == 0 or b == 0 or c == 0:
            print("Ошибка: Коэффициент не может быть равен 0. Попробуйте снова.")
        else:
            break
    except ValueError:
        print("Ошибка: Введите число в правильном формате (например: 2, 3.5, -1.75). Попробуйте снова.")

discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    x1 = (-b - discriminant ** 0.5) / 2 * a
    x2 = (-b + discriminant ** 0.5) / 2 * a
    print("Корни уравнения:")
    print("x1 =", x1)
    print("x2 =", x2)
elif discriminant == 0:
    x = -b / (2 * a)
    print("Корень уравнения:")
    print(x)
else:
    print("Корней нет.")
