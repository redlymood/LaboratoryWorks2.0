from math import *
def number1(n):
    a = int(input("Введите А "))
    b = int(input("Введите В "))
    if a != b:
        a = max(a, b)
        b = a
    else:
        a = 0
        b = 0
    print("Новые значения переменных:", a, b)

def number2(n):
    a = int(input("Введите А "))
    b = int(input("Введите В "))
    c = int(input("Введите С "))
    max1 = max(a, b, c)
    max2 = (a + b + c)  - min(a, b, c) - max(a, b, c)
    print("Сумма двух наибольших:", max1 + max2)

def number3(n):
    xa, ya = map(int, input("Введите координаты А через пробел ").split())
    xb, yb = map(int, input("Введите координаты B через пробел ").split())
    xc, yc = map(int, input("Введите координаты C через пробел ").split())
    ab = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
    ac = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
    if ab < ac:
        print("Точка В ближе к точке А, расстояние от А до В:", ab)
    elif ac < ab:
        print("Точка С ближе к точке А, расстояние от А до С:", ac)
    else:
        print("Точки В и С совпадают их расстояние до А:", ac)

def number4(n):
    x, y = map(int, input("Введите координаты точки через пробел ").split())
    if x * y > 0:
        if x > 0:
            print("Точка находится в первой четверти")
        else:
            print("Точка находится в третьей четверти")
    else:
        if x > 0:
            print("Точка находится в четвертой четверти")
        else:
            print("Точка находится во второй четверти")

def number5(n):
    a = int(input("Введите число "))
    if a % 2 == 0:
        if a > 0:
            print("Четное положительное число")
        elif a < 0:
            print("Четное отрицательное число")
        else:
            print("Нулевое число")
    else:
        if a > 0:
            print("Нечетное положительное число")
        else:
            print("Нечетное отрицательное число")

def number6(n):
    a = int(input("Введите число от 1 до 999 "))
    if a % 2 == 0:
        if a > 0 and a < 10:
            print("Четное однозначное")
        elif a >= 10 and a < 100:
            print("Четное двузначное")
        else:
            print("Четное трехзначное")
    else:
        if a > 0 and a < 10:
            print("Нечетное однозначное")
        elif a >= 10 and a < 100:
            print("Нечетное двузначное")
        else:
            print("Нечетное трехзнчное")

print("Для завершения введите 0")
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
    elif zadacha == 6:
        number6(zadacha)
    elif zadacha > 6 and zadacha < 0:
        print("Такой задачи нет")
