import statistics


def stats_calculator(*args, mode="basic"):
    if mode == "basic":
        basic(*args)
    elif mode == "advanced":
        advanced(*args)
    elif mode == "scientific":
        scientific(*args)


def basic(*args):
    print("Максимум:", max(args))
    print("Минимум:", min(args))
    print("Среднее арифметическое:", statistics.mean(args))


def advanced(*args):
    basic(*args)
    print("Медиана:", statistics.median(args))
    try:
        m = statistics.mode(args)
        print("Мода:", m)
    except statistics.StatisticsError:
        print("Нет уникальной моды.")


def scientific(*args):
    advanced(*args)
    try:
        g = statistics.geometric_mean(args)
        print("Среднее геометрическое:", g)
    except statistics.StatisticsError:
        print("Невозможно найти среднее геометрическое.")
    try:
        hm = statistics.harmonic_mean(args)
        print("Среднее гармоническое:", hm)
    except statistics.StatisticsError:
        print("Невозможно найти среднее гармоническое.")


def main():
    while True:
        try:
            nums = list(map(float, input("Введите числа для анализа (через пробел): ").split()))
            if len(nums) != 0:
                break
        except ValueError:
            print("Ошибка ввода данных. Пожалуйста, попробуйте снова.")

    mode = input("Выберите режим работы:\n1. basic\n2. advanced\n3. scientific\nВаш выбор: ")
    if mode in ["basic", "advanced", "scientific"]:
        stats_calculator(*nums, mode=mode)
    else:
        stats_calculator(*nums)


main()
