def number1(n):
    n = int(input("Введите длину массива: "))
    mas = [0] * n
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas[i] = int(input())
    for i in range(1, n):
        if mas[i] == mas[i - 1]:  #если текущий элемент равен предыдущему
            mas[i] = 'удалить'  #присваиваем текущему элементу значение удалить
    x = mas.count('удалить')  #считаем количество элементов, которые надо удалить
    for i in range(x):
        mas.remove('удалить')  #удаляем элементы, со значение удалить
    print("Результат", *mas)

def number2(n):
    n = int(input("Введите длину массива: "))
    mas = [0] * n
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas[i] = int(input())
    for i in range(n):
        if mas[i] != 'удалить':  #если мы еще не хотим удалить этот элемент
            if mas.count(mas[i]) == 2:  #считаем сколько раз он встречается в массиве
                a = mas[i]  #запоминаем значение в а, если этот элемент встречается 2 раза
                for j in range(n):  #запускаем цикл, чтобы присвоить дважды повторяющимся элементам значение удалить
                    if mas[j] == a:
                        mas[j] = 'удалить'
    x = mas.count('удалить')  #считаем сколько элементов надо удалить
    for i in range(x):
        mas.remove('удалить')  #удаляем элементы со значением удалить
    print("Результат", *mas)

def number3(n):
    n = int(input("Введите длину массива: "))
    mas = [0] * n
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas[i] = int(input())
    mas.insert(mas.index(min(mas)), 0)  #ищем индекс минимума, перед минимумом вставляем 0
    mas.insert(mas.index(max(mas)) + 1, 0)  #ищем индекс максимума, после максимума вставляем 0
    #сначала ищем минимум, а потом максимум, потому что если сначала будем искать максимум, то появившийся 0 после максимума станет минимальным
    print("Результат", *mas)

def number4(n):
    n = int(input("Введите длину массива: "))
    mas = [0] * n
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas[i] = int(input())
    ind = []  #создаем массив, где будут храниться индексы отрицательных элементов
    for i in range(len(mas)):
        if mas[i] < 0:
            ind.append(i)  #добавляем в массив индексы отрицательных элементов
    for i in range(len(ind)):
        mas.insert(ind[i] + 1, 0)  #добавляем после каждого отрицательного элемента 0
        for j in range(len(ind)):
            ind[j] += 1  #увеличиваем все индексы на единицу, тк массив увеличился на единицу
    print("Результат", *mas)

def number5(n):
    n = int(input("Введите длину массива: "))
    mas = [0] * n
    print("Введите каждый элемент массива с новой строки: ")
    for i in range(n):
        mas[i] = int(input())
    ind = []
    for i in range(len(mas)):
        if mas[i] > 0:
            ind.append(i)
    for i in range(len(ind)):
        mas.insert(ind[i], 0)
        for j in range(len(ind)):
            ind[j] += 1
    print("Результат", *mas)

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
