def number1(n):
    s = input('Введите строку ')
    flag = 0
    if s[0] == 'C':
        print('Последующий символ:', s[i + 1])
    else:
        for i in range(1, len(s) - 1):
            if s[i] == 'C':
                flag = 1
                print('Предшествующий символ:', s[i - 1], ', последующий символ:', s[i + 1])
                break
    if flag == 0 and s[-1] == 'C':
        print('Предшествующий символ:', s[i - 1])
    elif flag == 0:
        print('Символа С нет в строке')

def number2(n):
    s = input('Введите строку ')
    new = ''
    for i in range(len(s)):
        new += s[i] + ' '
    print('Новая строка', new)

def number3(n):
    s = input('Введите строку ')
    k = 0
    for i in range(len(s)):
        if s[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            k += 1
    print('Количество прописный букв:', k)

def number4(n):
    s = input('Введите строку ')
    new = ''
    for i in range(len(s)):
        if s[i] != 'C':
            new += s[i]
        else:
            new += s[i] + s[i]
    print('Строка с удвоение символа С:', new)

def number5(n):
    s = input('Введите строку s ')
    s0 = input('Введите строку s0 ')
    print('Количество вхождений строки s0 в строку s:', s.count(s0))

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
