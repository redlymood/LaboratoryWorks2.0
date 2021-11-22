def number1(n):
    n = int(input("Введите размер массива: "))
    mas = [0] * n
    k = 1
    for i in range(n):
        mas[i] = k
        k += 2
    print("Массив нечётных чисел:", mas)

def number2(n):
    n = int(input("Введите длину массива: "))
    a = int(input("Введите значение первого члена прогрессии: "))
    d = int(input("Введите знаменатель геометрической прогрессии: "))
    mas = [0] * n
    for i in range(n):
        mas[i] = a * d ** i
    print("Первые", n, "элементов геометрической прогрессии", mas)

def number3(n):
    n = int(input("Введите размер массива: "))
    a = int(input("Введите первый элемент массива: "))
    b = int(input("Введите второй элемент массива: "))
    mas = [0] * n
    mas[0] = a
    mas[1] = b
    for i in range(2, n):
        mas[i] = sum(mas)
    print(mas)

def number4(n):
    n = int(input("Введите размер массива: "))
    print("Введите все элементы массива, каждый элемент с новой строки: ")
    mas = []
    for i in range(n):
        mas.append(int(input()))
    for i in range(n // 2):
        print(mas[i])
        print(mas[n - i - 1])
    if n % 2 == 1:
        print(mas[n // 2])

def number5(n):
    n = int(input("Введите размер массива: "))
    mas = []
    print("Введите все элементы массива, каждый элемент с новой строки: ")
    for i in range(n):
        mas.append(int(input()))
    print("Элементы массива с нечётными индексами:")
    for i in range(1, n, 2):
        print(mas[i], end=' ')
    print()
    print("Элементы массива с чётными индексами:")
    for i in range(0, n, 2):
        print(mas[i], end=' ')

zadacha = 1
print("Для выхода введите 0")
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
