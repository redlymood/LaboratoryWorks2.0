def powerA3(a):
    b = a ** 3
    return b

def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

def ringS(r1, r2):
    return 3.14 * (r1 ** (0.5) - r2 ** (0.5))

def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3

def fact(n):
    f = 1
    if n % 2 == 0:
        k = 2
    else:
        k = 1
    while k <= n:
        f *= k
        k += 2
    return f

def number1(n):
    for i in range(5):
        a = float(input("Введите вещественное число: "))
        print("Третья степень:", powerA3(a))

def number2(n):
    a = float(input("Введите вещественное число А: "))
    b = float(input("Введите вещественное число В: "))
    print("Значение функции sign(a) + sign(b): ", sign(a) + sign(b))

def number3(n):
    for i in range(3):
        r1 = float(input("Введите радиус большей окружности: "))
        r2 = float(input("Введите радиус меньшей окружности: "))
        print("площадь кольца, заключенного между двумя окружностями с общим центром и радиусами:", ringS(r1, r2))

def number4(n):
    for i in range(3):
        x = int(input("Введите координату х: "))
        y = int(input("Введите координату у: "))
        print("Четверть, в которой находится точка", quarter(x, y))

def number5(n):
    n = int(input("Введите целое число: "))
    print("Двойной факториал:", fact(n))

zadacha = 1
while zadacha != 0:
    print()
    zadacha = int(input("Введите номер задачи "))
    if zadacha == 1:
        number1(zadacha)
    elif zadacha == 2:
        number2(zadacha)
    elif zadacha == 3:
        number3(zadacha)
    elif zadacha == 4:
        number4(zadacha)
    elif zadacha == 5:
        number5(zadacha)
    if zadacha > 5 and zadacha < 0:
        print("Такой задачи нет")
