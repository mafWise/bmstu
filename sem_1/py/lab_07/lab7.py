#Работа со списками. Ввод элементов в виде строк и различные действия над ними

import time
import math as m

def add(element, position = None):
    global s
    s.append(element)
    
#Функция дополненной проверки строки на числовую значимость
def is_digit_ver_2_0(t):
    if t[0] == '-':
        t = t[1:]
    if t.find('.') != 0:
        t = t.replace('.', '')
    return t.isdigit()

var0 = 'Выход из программы'
var1 = 'Очистить список и ввести его с клавиатуры'
var2 = 'Добавить элемент в произвольное место списка'
var3 = 'Удалить произвольный элемент из списка (по номеру)'
var4 = 'Очистить список'
var5 = 'Поиск элемента с наибольшим числом подряд идущих пробелов'
var6 = 'Замена двух подряд идущих цифр на последнюю цифру их суммы'

variants = (var0, var1, var2, var3, var4, var5, var6)
numbers = ('1','2','3','4','5','6','7','8','9','0')

size = 80
s = []

#Инициализация меню
while True:
    #Вывод таблицы с функциями
    print('\n|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
    for i in range(len(variants)):
        print('|' + '   {}|'.format(i) + '{0:^{1}}'.format(variants[i], size - 6) + '|')
        print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
    print('\n')
    print(s)
    #Ввод номера функции
    while True:
        var = input('Введите номер функции: ')    
        if is_digit_ver_2_0(var) == True and int(float(var)) <= 6 and int(float(var)) >= 0:
            break
        print('Ошибка')
    var = int(float(var))

    #Первая функция
    if var == 1:
        s.clear()
        while True:
            n = input('Введите количество элементов массива: ')
            if is_digit_ver_2_0(n) == True and int(float(n)) >= 0:    
                break
            print('Ошибка')    
        n = int(float(n))
        for i in range(n):
            el = input('Введите {}-ый элемент: '.format(i + 1))
            add(el)
    
    #Вторая функция
    elif var == 2:
        while True:
            n = input('Введите номер позиции элемента: ')
            if is_digit_ver_2_0(n) == True and int(float(n)) >= 1:
                break
            print('Ошибка')
        n = int(float(n))
        el = input('Введите элемент: ')
        add(el)
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
                
    #Третья функция
    elif var == 3:
        if len(s) >= 1:
            check = 0
            while True:
                n = input('Введите номер позиции элемента: ')
                if is_digit_ver_2_0(n) == True and int(float(n)) >= 1 and int(float(n)) <= len(s):
                    break
                print('Ошибка')
            n = int(float(n))
            f = s[-1]
            check = 1
            for i in range(len(s) - 1, 0, -1):
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
            if n == 1:
                del s[-1] 
        else: print('Ошибка')

    #Четвертая функция
    elif var == 4:
        s.clear()

    #Пятая функция
    elif var == 5:
        if len(s) >= 1:
            out = 'Таких элементов нет'
            MAX_qauntity = 0
            max_qauntity = 0
            for i in range(len(s)):
                quantity = 0
                for j in range(len(s[i])):
                    if s[i][j] == ' ':
                        quantity = quantity + 1
                    else:
                        if quantity > max_qauntity:
                            max_qauntity = quantity
                        quantity = 0
                if quantity > max_qauntity:
                    max_qauntity = quantity

                if max_qauntity > MAX_qauntity:
                    MAX_qauntity = max_qauntity
                    out = s[i]
                max_qauntity = 0
            print(out)
        else: print('Ошибка')
                 
    #Шестая функция
    elif var == 6:
        if len(s) >= 1:
            for i in range(len(s)):
                j = 0
                while j + 1 <= len(s[i]) - 1:
                    if s[i][j].isdigit() == True and s[i][j + 1].isdigit() == True:
                        s[i] = s[i].replace(s[i][j] + s[i][j + 1], str( ( int(s[i][j]) + int(s[i][j + 1]) ) % 10))
                    j += 1
        else: print('Ошибка')                    

    #Выход из программы
    elif var == 0:
        break
    time.sleep(1)
