from datetime import datetime


def check_dates(*dates):
    valid_dates = []
    future_dates = []
    today = datetime.today()
    for elem in dates:
        try:
            new_date = datetime.strptime(elem, '%d.%m.%Y')
            valid_dates.append(new_date)
            if new_date > today:
                future_dates.append(new_date)
        except ValueError:
            print(f"{elem} - некорректная дата.")

    if len(valid_dates) != 0:
        print("Найдено корректных дат:", len(valid_dates))
        k = 1
        for i in valid_dates:
            print(f"{k})", i.strftime("%d.%m.%Y"))
            k += 1
        print("Самая ранняя дата:", min(valid_dates).strftime("%d.%m.%Y"))
        print("Самая поздняя дата", max(valid_dates).strftime("%d.%m.%Y"))
        if len(future_dates) != 0:
            l = 1
            print("Будущие даты:")
            for j in future_dates:
                print(f"{l})", j.strftime("%d.%m.%Y"))
                l += 1
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
        while True:
            try:
                date = input("Введите дату в формате DD.MM.YYYY: ")
                if date.count(".") == 2:
                    dates.append(date)
                    break
                else:
                    print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")
            except ValueError:
                print("bad")
    check_dates(*dates)


main()
