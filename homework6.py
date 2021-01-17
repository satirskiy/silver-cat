while True:
    day = 1
    firstday = float(input("Введите результат в первый день:"))
    result = float(input("Введите финальный результа:"))
    if firstday <= 0 or result <= 0:
        print("Вы ввели не верное значетие!")
    else:
        while result > firstday:
            firstday += firstday * 0.1
            day += 1


        print(day)
        break



