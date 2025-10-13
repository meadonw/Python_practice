from statistics import mean, median, mode, geometric_mean, harmonic_mean


def stats_calculator(*args, mode):
    if mode == 1:
        basic(*args)
    elif mode == 2:
        advanced(*args)
    elif mode == 3:
        scientific(*args)


def basic(*args):
    print("Максимум:", max(args))
    print("Минимум:", min(args))
    print("Среднее арифметическое:", mean(args))


def advanced(*args):
    basic(*args)
    print("Медиана:", median(args))
    print("Мода:", mode(args))


def scientific(*args):
    advanced(*args)
    print("Среднее геометрическое:", geometric_mean(args))
    print("Среднее гармоническое:", harmonic_mean(args))


def main():
    while True:
        try:
            nums = list(map(int, input("Введите числа для анализа (через пробел): ").split()))
            if len(nums) != 0:
                break
        except ValueError:
            print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")
    while True:
        try:
            mode = int(input("Выберите режим работы:\n1. basic\n2. advanced\n3. scientific\nВаш выбор (1-3): "))
            if 1 <= mode <= 3:
                break
            else:
                print("Ошибка. Введите число от 1 до 3!")
        except ValueError:
            print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")
    stats_calculator(*nums, mode=mode)


main()
