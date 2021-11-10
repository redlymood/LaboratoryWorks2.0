from math import *
def number1(n):
    a = int(input("Введите А "))
    b = int(input("Введите В "))
    if a > 2 and b <= 3:
        print("Неравенства А > 2 и В <= 3 справедливы")
    else:
        print("Неравенства А > 2 и В <= 3 не справедливы")

def number2(n):
    a = int(input("Введите А "))
    b = int(input("Введите В "))
    c = int(input("ВВедите С "))
    if a < b and b < c:
        print("Двойное неравенство А < В < С справедливо")
    else:
        print("Двойное неравенство А < В < С не справедливо")

def number3(n):
    a = int(input("Введите А "))
    print("Данное число является чётным и двузначным:", end=' ')
    if a % 2 == 0:
        print("истина")
    else:
        print("ложь")

def number4(n):
    a = int(input("Введите трёхзначное число: "))
    a = str(a)
    if a[0] > a[1] > a[2]:
        print("Цифры данного числа образуют убывающую последовательность")
    elif a[0] < a[1] < a[2]:
        print("Цифры данного числа образуют возрастающую последовательность")
    else:
        print("Цифры данного числа не образуют возрастающую или убывающую последовательности")

def number5(n):
    a = int(input("Введите четырёхзначное число: "))
    a = str(a)
    if a[0] == a[3] and a[1] == a[2]:
        print("Число", a, "палиндром")
    else:
        print("Число", a, "не палиндром")

def number6(n):
    print("Введите стороны треугольника: ")
    a = int(input())
    b = int(input())
    c = int(input())
    if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + c ** 2:
        print("Треугольник прямоугольный")
    else:
        print("Треугольник не прямоyгольный")

def number7(n):
    print("Введите стороны треугольника: ")
    a = int(input())
    b = int(input())
    c = int(input())
    if a < b + c and c < b + a and b < a + c:
        print("Треугольник с такими сторонами существует")
    else:
        print("Треугольника с такими сторонами не существует")

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
    elif zadacha == 7:
        number7(zadacha)
    elif zadacha > 7 and zadacha < 0:
        print("Такой задачи нет")
