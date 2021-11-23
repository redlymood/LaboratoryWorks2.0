def number1(n):
    n = int(input("Введите длину массива: "))
    a = [0] * n
    b = [0] * n
    print("Введите каждый элемент массива A с новой строки: ")
    for i in range(n):
        a[i] = int(input())
    print("Введите каждый элемент массива B с новой строки: ")
    for i in range(n):
        b[i] = int(input())
    a, b = b, a
    print("Массив А:", *a)
    print("Массив В:", *b)

def number2(n):
    n = int(input("Введите длину массива: "))
    a = [0] * n
    b = [0] * n
    print("Введите каждый элемент массива A с новой строки: ")
    for i in range(n):
        a[i] = int(input())
    for i in range(1, n):
        s = 0
        k = 0
        for j in range(1, i + 1):
            s += a[j]
            k += 1
        b[i] = s / k
    print("Массив В:", *b)

def number3(n):
    n = int(input("Введите длину массива: "))
    mas = []
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas.append(int(input()))
    a = 0
    for i in range(n):
        if mas[i] % 2 == 1:
            a = mas[i]
    for i in range(n):
        if mas[i] % 2 == 1:
            mas[i] += a
    print("Результат:", *mas)

def number4(n):
    n = int(input("Введите длину массива: "))
    mas = [0] * n
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas[i] = int(input())
    maxx = mas.index(max(mas))  #находим индекс максимального элемента
    minn = mas.index(min(mas))  #находим индекс минимального элемента
    if maxx < minn:  #если индекс максимального, меньше минимального, то меняем их местами, чтобы удобнее было задать диапазон
        maxx, minn = minn, maxx
    for i in range(minn + 1, maxx):  #перебираем все числа от меньшего индекса к большему не включая края
        mas[i] = 0
    print("Резельтат:", *mas)

def number5(n):
    n = int(input("Введите длину массива: "))
    mas = [0] * n
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas[i] = int(input())
    a = mas[0]  #запоминаем нулевой элемент
    for i in range(1, n):
        if a > mas[i]:  #двигаем каждый элемент, который меньше нулевого на 1 влево
            mas[i - 1] = mas[i]
        else:  #когда встретим элемент, который больше или равен а, то на место предыдущего вставим значение а
            mas[i - 1] = a
            break
    print("Результат:", *mas)

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
