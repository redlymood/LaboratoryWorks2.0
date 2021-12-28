def number1(n):
    s = input('Введите строку: ').split()
    print('Количество слов:', len(s))

def number2(n):
    s = input('Введите строку: ').split()
    lenght = []
    for i in range(len(s)):
        s[i].strip()
        lenght.append(len(s[i]))
    print('Минимальная длина слова в строке:', min(lenght))

def number3(n):
    s = input('Введите строку: ').split()
    for i in range(len(s)):
        a = s[i]
        first = a[0]
        a = a[1::]
        s[i] = first + a.replace(first, '.')
    print('Результат', *s)

def number4(n):
    s = input('Введите строку: ')
    k = 0
    for i in range(len(s)):
        if s[i] in 'уеыаоэёяию':
            k += 1
    print('Количество гласных в строке: ', k)

def number5(n):
    s = input().split('/')
    a = s[-1].split('.')
    print('Имя файла: ', a[0])

def number6(n):
    s = input('Введите строку: ').split('/')
    if len(s) == 2:
        print('/')
    else:
        print(s[-2])

def number7(n):
    s = input('Введите строку: ')
    new = ''
    for i in range(1, len(s), 2):
        new += s[i]
    for i in range(len(s), 0, -2):
        new += s[i]
    print('Зашифрованная строка', new)

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
    elif zadacha == 6:
        number6(zadacha)
    elif zadacha == 7:
        number7(zadacha)
    if zadacha > 7 and zadacha < 0:
        print("Такой задачи нет")
