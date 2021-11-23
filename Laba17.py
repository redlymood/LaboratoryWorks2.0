def number1(n):
    n = int(input("Введите длину массива: "))
    k = int(input("Введите К: "))
    l = int(input("Введите L: "))
    mas = []
    s = 0
    cnt = 0
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas.append(int(input()))
    for i in range(k, l + 1):
        s += mas[i]  #подсчитываем сумму элементов
        cnt += 1  #подсчитываем количество элементов
    print("Среднее арифметическое элементов: ", s / cnt)

def number2(n):
    n = int(input("Введите длину массива: "))
    mas = []
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas.append(int(input()))
    d = mas[1] - mas[0]  #считаем разность арифметической прогрессии
    for i in range(2, n):
        if mas[i] - mas[i - 1] != d:  #если текущая разность не равна самой первой, то последовательность не арифметическая, ломаем цикл
            d = 0
            break
    print(d)

def number3(n):
    n = int(input("Введите длину массива: "))
    mas = []
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas.append(int(input()))
    minn = 10 ** 30
    for i in range(2, n, 2):  #делаем цикл, которые пережирает только четные индексы начиная с 2
        minn = min(minn, mas[i])  #ищем минимум из элементов с четными индексами
    print(minn)

def number4(n):
    n = int(input("Введите длину массива: "))
    mas = []
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas.append(int(input()))
    maxx = -1  #присваием переменной значение -1 на случай, если не встретим локальный максимум
    if mas[0] > mas[i]:  #проверяем может ли нулевой элемент быть локальным максимумом
        maxx = 0
    for i in range(1, n - 1):  #запускаем цикл6 где проверяем остальные элементы на локальный максимум
        if mas[i] > mas[i - 1] or mas[i] > mas[i + 1]:
            maxx = i
    if mas[n - 1] > mas[n - 2]:  #проверяем может ли последний элемент быть локальым максимумом
        maxx = n - 1
    if maxx == -1:  #если переменная так и не изменила свое значение, то локального максимума нет
        print("Локального максимума нет")
    else:
        print("Номер последнего локального максимума (нумерация с нуля):", maxx)

def number5(n):
    n = int(input("Введите длину массива: "))
    mas = []
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas.append(int(input()))
    for i in range(n - 1):
        if mas[i] == mas[i + 1]:
            i1 = i
            i2 = i + 1
    print("Номера одинковых элементов (нумерация с нуля):", i1, i2)

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
