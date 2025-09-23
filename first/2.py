while True:
    try:
        digit_summ = int(input("Введите целое число от 1 до 27 (сумму цифр): "))
        if 1 > digit_summ or digit_summ > 27:
            print("Пожалуйста, введите число от 1 до 27.")
        else:
            break
    except ValueError:
        print("Ошибка: Вы не ввели число. Пожалуйста, попробуйте снова.")

for n in range(100, 1000):
    if n // 100 + n % 100 // 10 + n % 10 == digit_summ:
        print(n)
