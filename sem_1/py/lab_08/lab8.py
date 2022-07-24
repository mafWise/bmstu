#Работа со списками. Ввод элементов в виде строк и различные действия над ними

import time
import math as m

#Функция дополненной проверки строки на числовую значимость
def isDigit(t):
    if t[0] == '-':
        t = t[1:]
    if t.find('.') != 0:
        t = t.replace('.', '')
    return t.isdigit()

#lin_row - строка или столбец, el - элемент, n - индекс
def add(line_row, el, n):
    global s
    global way
    if line_row == 'line':
        if way == 'A':
            s.append(el)
            for i in range(len(s) - 1):
                if i == n - 1:
                    f = s[i + 1]
                    s[i + 1] = s[i]
                    s[i] = el
                    check = 1
                elif i > n - 1:
                    if check == 1:
                        k = s[i + 1]
                        s[i + 1] = f
                        check = 0
                    elif check == 0:
                        f = s[i + 1]
                        s[i + 1] = k
                        check = 1
        elif way == 'P':
            s.insert(n - 1, el)
    elif line_row == 'row':
        if way == 'A':
            for i in range(len(s)):
                s[i].append(el[i])
                for j in range(len(s[i]) - 1):
                    if j == n - 1:
                        f = s[i][j + 1]
                        s[i][j + 1] = s[i][j]
                        s[i][j] = el[i]
                        check = 1
                    elif j > n - 1:
                        if check == 1:
                            k = s[i][j + 1]
                            s[i][j + 1] = f
                            check = 0
                        elif check == 0:
                            f = s[i][j + 1]
                            s[i][j + 1] = k
                            check = 1
        elif way == 'P':
            for i in range(len(s)):
                s[i].insert(n - 1, el[i])

def rem(line_row, n):
    global s
    global way
    if line_row == 'line':
        if way == 'A':
            f = s[-1]
            check = 1
            for i in range(len(s) - 1, 0, -1):
                if n == 1:
                    del s[0]
                    break
                if i == n - 1:
                    del s[-1]
                    break
                elif i > n - 1:
                    if check == 1:
                        k = s[i - 1]
                        s[i - 1] = f
                        check = 0
                    elif check == 0:
                        f = s[i - 1]
                        s[i - 1] = k
                        check = 1
        elif way == 'P':
            del s[n - 1]
    elif line_row == 'row':
        if way == 'A':
            for i in range(len(s)):
                f = s[i][-1]
                check = 1
                for j in range(len(s[i]) - 1, 0, -1):

                    if n == 1:
                        del s[i][0]
                        break
                    if j == n - 1:
                        del s[i][-1]
                        break
                    elif j > n - 1:
                        if check == 1:
                            k = s[i][j - 1]
                            s[i][j - 1] = f
                            check = 0
                        elif check == 0:
                            f = s[i][j - 1]
                            s[i][j - 1] = k
                            check = 1

        elif way == 'P':
            for i in range(len(s)):
                del s[i][n - 1]

varmin1 = 'Выйти из программы'
var0 = 'Вывести текущую матрицу'
var1 = 'Ввести матрицу'
var2 = 'Добавить строку'
var3 = 'Удалить строку'
var4 = 'Добавить столбец'
var5 = 'Удалить столбец'
var6 = 'Найти строку, имеющую наименьшее количество четных элементов'
var7 = 'Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов'
var8 = 'Найти столбец, имеющий наибольшее количество чисел, являющихся степенями 2'
var9 = 'Переставить местами столбцы с максимальной и минимальной суммой элементов'
varA = 'Переключить реализацию пунктов 2-5 на алгоритмическую'
varP = 'Переключить реализацию пунктов 2-5 на методом Python'

variants = (varmin1, var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, varA, varP)
symbols = ('-1', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'P')
s = []
size = 120

way = 'A'
#Инициализация меню
while True:
    #Вывод таблицы с функциями
    print('\n|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
    for i in range(len(symbols)):
        print('|' + '{:^4}|'.format(symbols[i]) + '{0:^{1}}'.format(variants[i], size - 6) + '|')
        print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
    print('\nМетод реализации - ', way)
    for i in range(len(s)):
        print(s[i])
    #Ввод номера функции
    while True:
        var = input('\nВведите номер функции: ')
        if var in symbols:    
            break
        print('Ошибка')

    if var == '1':
        s.clear()
        while True:
            n = input('Введите количество строк матрицы: ').strip()
            if isDigit(n) == True and int(float(n)) >= 0:    
                break
            print('Ошибка')    
        n = int(float(n))
        l_row = n
        for i in range(n):
            while True:
                m = list(map(str, input('Введите {}-ую строку: '.format(i + 1)).strip().split()))
                if i == 0:
                    l_line = len(m)
                check = 1
                for j in m:
                    if isDigit(j) != True or len(m) != l_line:
                        check = 0
                        print('Ошибка')
                        break
                if check == 1:
                    if i == 0:
                        l_line = len(m)
                    s.append(list(map(int, m)))
                    break

    elif var == '2':
        while True:
            n = input('Введите номер позиции строки: ')
            if isDigit(n) == True and int(float(n)) >= 1:
                break
            print('Ошибка')
        n = int(float(n))
        while True:
            check = 1
            m = list(map(str, input('Введите строку: ').strip().split()))
            for j in m:
                if isDigit(j) != True or len(m) != len(s[0]):
                    check = 0
                    print('Ошибка')
                    break
            if check == 1:
                break
        print(m)
        add('line', list(map(int, m)), n)

    elif var == '3':
        if len(s) >= 1:
            while True:
                n = input('Введите номер позиции строки: ')
                if isDigit(n) == True and int(float(n)) >= 1 and int(float(n)) <= len(s):
                    break
                print('Ошибка')
            n = int(float(n))
            rem('line', n)
        else:
            print('Ошибка')
    elif var == '4':
        while True:
            n = input('Введите номер позиции столбца: ')
            if isDigit(n) == True and int(float(n)) >= 1:
                break
            print('Ошибка')
        n = int(float(n))
        while True:
            check = 1
            m = list(map(str, input('Введите элементы столбца: ').strip().split()))
            for j in m:
                if isDigit(j) != True or len(m) != len(s):
                    check = 0
                    print('Ошибка')
                    break
            if check == 1:
                break
        print(m)
        add('row', list(map(int, m)), n)

    elif var == '5':
        if len(s) >= 1:
            while True:
                n = input('Введите номер позиции столбца: ')
                if isDigit(n) == True and int(float(n)) >= 1 and int(float(n)) <= len(s[0]):
                    break
                print('Ошибка')
            n = int(float(n))
            rem('row', n)
        else:
            print('Ошибка')

    elif var == '6':
        min_count = 1000000
        min_index = 0
        count = 0
        for i in range(len(s)):
            count = len(list(filter(lambda x: x % 2 == 0, s[i])))
            if count < min_count:
                min_count = count
                min_index = i
                count = 0
        print(s[min_index])

    elif var == '7':
        min_count = 1000000
        max_count = -1
        count = 0
        min_index = 0
        max_index = 0
        for i in range(len(s)):
            count = len(list(filter(lambda x: x < 0, s[i])))
            if count > max_count:
                max_count = count
                max_index = i
                count = 0
            elif count < min_count:
                min_count = count
                min_index = i
                count = 0
        s[max_index], s[min_index] = s[min_index], s[max_index]
    
    elif var == '8':
        max_count = -1
        max_index = 0
        for i in range(len(s[0])):
            count = 0
            for j in range(len(s)):
                if bin(s[j][i]).count('1') == 1:
                    count += 1
            if count > max_count:
                print(count)
                max_count = count
                max_index = i
                print(i)
                count = 0
        print( [ s[i][max_index] for i in range(len(s))] )

    elif var == '9':
        max_count = -1
        min_count = 1000000
        max_index = 0
        min_index = 0
        count = 0
        for j in range(len(s[0])):
            count = sum([s[i][j] for i in range(len(s))])
            if count > max_count:
                max_count = count
                max_index = j
                count = 0
            elif count < min_count:
                min_count = count
                min_index = j
                count = 0
        for i in range(len(s)):
            s[i][min_index], s[i][max_index] = s[i][max_index], s[i][min_index]     

    elif var == 'A': way = 'A'
    
    elif var == 'P': way = 'P'

    elif var == '-1': exit()
    
    elif var == '0': print(s)
    
    else: print('Ошибка')
    time.sleep(1)
            
