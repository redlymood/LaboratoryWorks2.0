def number1(n):
    name = input('Введите полное имя файла ')
    f = open(name)
    s = f.readline().split()
    f.close()
    s = s[1:]
    s = ' '.join(s)
    with open(name, 'w') as file:
        file.writelines(s)

def number2(n):
    name = input('Введите полное имя файла ')
    n = int(input('Введите количество строк '))
    k = int(input('Введите количество символов в строке '))
    with open(name, 'w') as file:
        for i in range(n):
            file.writelines('*' * k)
            file.writelines('\n')

def number3(n):
    name1 = input('Введите полное имя файла 1 ')
    name2 = input('Введите полное имя файла 2 ')
    with open(name1, 'a') as file1, open(name2, 'r') as file2:
        for line in file2:
            file1.write(line)

def number4(n):
    name = input('Введите полное имя файла ')
    with open(name, 'r') as file1, open('copy.txt', 'w') as file2:
        for line in file1:
            a = line.split()
            for i in range(len(a)):
                a[i] = a[i].strip()
            a = ' '.join(a)
            file2.writelines(a + '\n')
    file1.close()
    file2.close()
    with open(name, 'w') as file3, open('copy.txt', 'r') as file4:
        for line in file4:
            file3.writelines(line + '\n')

def number5(n):
    name = input('Введите полное имя файла ')
    f = open(name)
    x = f.readlines()
    f.close()
    n = 0
    for i in x:
        if i[:5] == '     ' and i[5] != ' ' and i[5:] != '\n':
            n += 1
    print('Количество абзацев:', n)

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
