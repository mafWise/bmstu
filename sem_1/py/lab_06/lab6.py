#Работа со списками. Ввод числовым значений и использование разных функций

import time
import math as m

#Функция проверка числа на простоту
def is_prime(t):
    check = 0
    for i in range(2, int(abs(t)) // 2 + 1):
        if abs(t) % i == 0:
            check = 1
    if check == 0:
        return True

#Функция дополненной проверки строки на числовую значимость
def is_digit_ver_2_0(t):
    if t[0] == '-':
        t = t[1:]
    if t.find('.') != 0:
        t = t.replace('.', '')
    return t.isdigit()

var1 = 'Проинициализировать список первыми N элементами заданного ряда'
var2 = 'Очистить список и ввести его с клавиатуры'
var3 = 'Добавить элемент в произвольное место списка'
var4 = 'Удалить произвольный элемент из списка (по номеру)'
var5 = 'Очистить список'
var6 = 'Найти значение k-го экстремума в списке'
var7 = 'Найти наиболее длинную возрастающую последовательность отрицательных чисел, модуль которых является простым числом'

variants = (var1, var2, var3, var4, var5, var6, var7)

size = 120
s = []

#Инициализация меню
while True:
    #Вывод таблицы с функциями
    print('\nДля выхода из программы введите "-1"\nДля показа массива введите "0"')
    print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
    for i in range(7):
        print('|' + '   {}|'.format(i + 1) + '{0:^{1}}'.format(variants[i], size - 6) + '|')
        print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
    #Ввод номера функции
    while True:
        var = input('\nВведите номер функции: ')    
        if is_digit_ver_2_0(var) == True and int(float(var)) <= 7 and int(float(var)) >= -1:
            break
    var = int(float(var))

    #Первая функция
    if var == 1:
        while True:
            n = input('Введите количество элементов массива: ')
            if is_digit_ver_2_0(n) == True and int(float(n)) > 0:
                break
        n = int(float(n))
        while True:
            x = input('Введите значение x: ')
            if is_digit_ver_2_0(x) == True:
                break
        x = float(x)
        for i in range(1, n):
            s.append( (x**i) / m.factorial(i) )
        s.insert(0, 1)
    
    #Вторая функция
    elif var == 2:
        s.clear()
        while True:
            n = input('Введите количество элементов массива: ')
            if is_digit_ver_2_0(n) == True and int(float(n)) >= 0:
                break
        n = int(float(n))
        for i in range(n):
            while True:
                a = input('Введите {}-ый элемент: '.format(i + 1))
                if is_digit_ver_2_0(a) == True:
                    break
            s.append(float(a))
                
    #Третья функция
    elif var == 3:
        check = 0
        while True:
            n = input('Введите номер позиции элемента: ')
            if is_digit_ver_2_0(n) == True and int(float(n)) > 1:
                break
        n = int(float(n))
        while True:
            while True:
                a = input('Введите элемент: ')
                if is_digit_ver_2_0(a) == True:
                    break
            a = float(a)
            s.insert(int(float(n)) - 1, float(a))
            check = 1
            if check == 1:
                break

    #Четвертая функция
    elif var == 4:
        if (len(s)) != 0:
            while True:
                n = input('Введите номер позиции элемента: ')
                if is_digit_ver_2_0(n) == True and int(float(n)) <= len(s): 
                    break
            del s[int(float(n))-1]

        else:
            print('Ошибка')
    
    #Пятая функция
    elif var == 5:
        s.clear()
    
    #Шестая функция
    elif var == 6:
        if len(s) >= 3:
            check = 0
            while True:
                k = input('Введите значение k: ')
                if is_digit_ver_2_0(k) == True and int(float(k)) > 0:
                    break
            k = int(float(k))
            for i in range(1, len(s) - 1):
                if (s[i] < s[i - 1] and s[i] < s[i + 1]) or (s[i] > s[i - 1] and s[i] > s[i + 1]):
                    check += 1
                    if check == k:
                        print('Значение {}-го экстремума в списке: {}'.format(k, s[i]))
                        check = -2
                        break
            if check == -2:
                time.sleep(1.5)
                continue
            elif check == 0:
                print('В данном списке нет экстремума')    
            else:
                print('В списке нет {}-ого значения экстремума'.format(k))
        else:
            print('Ошибка')
        time.sleep(1.5)

    #Седьмая функция
    elif var == 7 and len(s) > 0:
        n = 1
        max_n = -1
        for i in range(1, len(s)):
            if s[i] < 0 and s[i - 1] < 0 and s[i] > s[i - 1] and (is_prime(abs(s[i])) == True) and (is_prime(abs(s[i - 1])) == True):
                n += 1
            else:
                max_n = n
                n = 1
        print('Наиболее длинная последовательность равна {}'.format(max_n))
    
    #Вывод массива
    elif var == 0:
        print(s)
        time.sleep(1.5)
        continue
    
    #Выход из программы
    elif var == -1:
        break

    print('Массив = ', s)
    time.sleep(1.5)
