from datetime import datetime


def check_dates(*dates):
    valid_dates = []
    future_dates = []
    today = datetime.today()
    for elem in dates:
        try:
            new_date = datetime.strptime(elem, '%d.%m.%Y')
            valid_dates.append(new_date)
        except ValueError:
            print(f"{elem} - некорректная дата.")
    for date in valid_dates:
        if date > today:
            future_dates.append(date)

    if len(valid_dates) != 0:
        print("Найдено корректных дат:", len(valid_dates))
        n = 1
        for i in valid_dates:
            print(f"{n})", i.strftime("%d.%m.%Y"))
            n += 1
        print("Самая ранняя дата:", min(valid_dates).strftime("%d.%m.%Y"))
        print("Самая поздняя дата", max(valid_dates).strftime("%d.%m.%Y"))
        if len(future_dates) != 0:
            n = 1
            print("Будущие даты:")
            for j in future_dates:
                print(f"{n})", j.strftime("%d.%m.%Y"))
                n += 1
        else:
            print("Не найдено ни одной из будущих дат.")
    else:
        print("Не найдено ни одной корректной даты.")


def main():
    while True:
        try:
            n = int(input("Введите кол-во сгенерированных дат: "))
            if n > 0:
                break
            else:
                print("Ошибка. Число должно быть положительным.")
        except ValueError:
            print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")
    dates = []
    for _ in range(n):
        date = input("Введите дату в формате DD.MM.YYYY: ")
        dates.append(date)
    check_dates(*dates)


main()
