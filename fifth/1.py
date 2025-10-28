import random


def main():
    while True:
        try:
            n = int(input("Введите длину списка: "))
            if n > 0:
                break
            else:
                print("Ошибка. Длина должна быть > 0.")
        except ValueError:
            print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")

    lst = [random.randint(-100, 100) for x in range(n)]
    answer = list(filter(lambda x: x > (sum(lst) / len(lst)), lst))
    print("Исходный список:", lst)
    if len(answer) == 0:
        print("Не найдено ни одного подходящего элемента.")
    else:
        print("Элементы, значения которых превышает среднее арифметическое списка:", answer)


main()
