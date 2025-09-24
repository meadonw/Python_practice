while True:
    try:
        deposit_size = float(input("Введите начальную сумму вклада (руб.): "))
        interest_rate = float(input("Введите годовую процентную ставку (%): "))
        years = int(input("Введите количество лет: "))
        if deposit_size <= 0 or interest_rate <= 0 or years <= 0:
            print("Ошибка: входные данные должны быть положительны. Попробуйте снова.")
        else:
            break
    except ValueError:
        print("Введите данные в правильном формате.")

print("Год --- Сумма")
for year in range(1, years + 1):
    deposit_size *= 1 + (interest_rate / 100)
    print(f"{year} --- {round(deposit_size, 2)}")
