def number1(n):
    a = float(input("Введите вещественное число А "))
    for i in range(1, 11):
        print("Стоимость", i / 10, "кг конфет", a * (i / 10))

def number2(n):
    n = int(input("Введите целое число N "))
    p = 1
    for i in range(1, n + 1):
        p *= (1 + (i / 10))
    print("Произведение сомножителей:", p)

def number3(n):
    n = int(input("Введите целое число N "))
    res = 0
    for i in range(1, 2 * n, 2):
        res += i
        print(res)

def number4(n):
    a = float(input("Введите вещественное число А "))
    n = int(input("Введите целое число N "))
    s = 0
    for i in range(n):
        s += a ** i
    print("Сумма:", s)

def number5(n):
    a = float(input("Введите вещественное число А "))
    n = int(input("Введите целое число N "))
    s = 0
    for i in range(n):
        s += (-a) ** i
    print("Сумма:", s)

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
    elif zadacha > 5 and zadacha < 0:
        print("Такой задачи нет")
