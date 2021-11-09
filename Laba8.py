from math import *
def number1(n):
    byte = int(input("Введите количество байт "))
    print(byte, "байт = ", ceil(byte / 8), "килобайт")
def number2(n):
    a = int(input("Введите длинну отрезка А "))
    b = int(input("Введите длинну отрезка В "))
    print(a // b, "B помещается на отрезке A")
def number3(n):
    a = int(input("Введите длинну отрезка А "))
    b = int(input("Введите длинну отрезка В "))
    print("Длина незанятого отрезка А:", a % b)
def number4(n):
    a = int(input("Введите двузначное число "))
    print("Число, полученное при перестановке цифр:", a % 10 * 10 + a // 10)
def number5(n):
    a = int(input("Введите трехзначное число "))
    print("Результат:", a % 100 * 10 + a // 100)
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
    else:
        print("Такой задачи нет")
