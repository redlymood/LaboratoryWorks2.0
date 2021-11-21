from math import *
def number1(n):
    a = int(input("Введите целое положительное А: "))
    b = int(input("Введите целое положительное В > А: "))
    for i in range(a, b + 1):
        s = str(i)
        print(s * i, sep=' ')

def number2(n):
    k = 0
    a = int(input("Введите длину отрезка А: "))
    b = int(input("Введите длинну отрезка В < А: "))
    while a > 0:
        if a - b >= 0:
            k += 1
        a -= b
    print(k, "отрезков В помещаются на отрезке А")

def number3(n):
    m = int(input("Введите целое число N: "))
    s = 0
    k = 1
    while s < m:
        s += k
        k += 1
    print(k - 1)

def number4(n):
    p = float(input("Введите процент на который ежемесячно увеличивается вклад: "))
    k = 0
    s = 1000
    while s <= 1100:
        k += 1
        s += 1 + (p / 100)
    print("Через", k, "месяцев вклад будет", s, "рублей")

def number5(n):
    a = int(input("Введите целое положительное А: "))
    b = int(input("Введите целое положительное В: "))
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print("Наибольший общий делитель:", a)

def number6(n):
    m = int(input("Введите число Фибоначчи "))
    tek = 1
    last = 1
    k = 2
    while tek != m:
        k += 1
        tek, last = tek + last, tek
    print(m, "является", k, "в последовательности")

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
