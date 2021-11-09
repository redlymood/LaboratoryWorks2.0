from math import *
def number1(n):
    seconds = int(input("Введите количество секунд "))
    print("Количество секунд, прошедших с начала последней минуты:", seconds % 60)

def number2(n):
    k = int(input("Введите К 1-365 "))
    mas = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    print(mas[k % 7])

def number3(n):
    k = int(input("Введите K 1-365 "))
    m = int(input("Введите N 0-7 "))
    mas = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    print(mas[(k - m) % 7])

def number4(n):
    a = int(input("Введите длину прямоугольника "))
    b = int(input("Введите ширину прямоугольника "))
    c = int(input("Введите сторону квадрата "))
    print((a * b) // (c ** 2), "квадратов помещается в прямоугольнике")
    print((a * b) % (c ** 2), "незанятая площадь")

def number5(n):
    year = int(input("Введите номер года "))
    print("Номер столетия", (year - 1) // 100 + 1)

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
