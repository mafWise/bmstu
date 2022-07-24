from os import path

"""
Работа с файлами. Инициализирование БД. 
"""

#Функция проверка символа на числовую значимость
def isDigit(t):
    if t == '': return False
    if t[0] == '-':
        t = t[1:]
    if t.find('.') != 0:
        t = t.replace('.', '')
    return t.isdigit()

#Проверка строки на числовую значимость
def digit_input(stroke):
    while True:
        n = input(stroke).strip()
        if isDigit(n) == True and float(n) >= 0:
            return int(float(n))
        print('Введенный символ не является числом или является числом не положительным. Повторите ввод')

#Доступные возможности программы
variants = (
    'Выбрать файл для работы',
    'Инициализировать базу данных',
    'Вывести содержимое базы данных',
    'Добавить запись в базу данных',
    'Поиск по одному полю',
    'Поиск по двум полям',
)
 
file = None #Путь к файлу
size = 90 #Ширина таблички
size_db = 90
size_db_orig = size_db

types = ('int', 'str') #Поддерживаемые типы данных

#Вывод таблички
print('\nДоступные коды программ:\n')
print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
for i in range(len(variants)):
    print('|' + '{:^4}|'.format(i + 1) + '{0:^{1}}'.format(variants[i], size - 6) + '|')
    print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
print('Для вывода таблички введите 0\n')

while True:
    #Ввод кода программы
    var = digit_input('Введите код: ')

    #Код вывода таблички
    if var == 0:
        print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
        for i in range(len(variants)):
            print('|' + '{:^4}|'.format(i + 1) + '{0:^{1}}'.format(variants[i], size - 6) + '|')
            print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
        print('')

    #Ввод пути к файлу
    if var == 1:
        file = input('Введите полный или относительный путь к файлу: ')
        check = True

        if path.isfile(file) and file[-3:] == 'txt':
            database = open(file, 'a+')
            database.seek(0, 0)
            row = database.readline().replace(' ', '')[:-1]
            if '|' in row:
                check = False
                fields = row.split('|')
                for i in range(len(fields)):
                    fields[i] = fields[i].split('-')
                size_db = size_db // len(fields)
            else:
                print('Необходима инициализация БД')
                database.close()
        else:
            print('Необходима инициализация БД')
            
    #Инициализация БД
    elif var == 2:
        if file is None:
            print('Не выбран файл для инициализации БД')
            continue
    
        if check == True:
            database = open(file, 'w+')
            fields = []
            whole_row = ''
            for i in range(digit_input('Введите количество полей: ')):
                while True:
                    row = input('Введите имя {}-ого поля и его тип данных через пробел: '.format(i+1)).split()
                    if len(row) != 2:
                        print('Данные введены неверно. Повторите ввод')
                        continue
                    if row[1] in types:
                        break
                    print('Неверный тип данных. Повторите ввод')
                fields.append(row)

            size_db = size_db // len(fields)
            write = ''
            for el in fields:
                write += '{:^{}}|'.format('{:} - {:}'.format(el[0], el[1]), size_db)
            write = write[:-1] + '\n'
            streak = ''
            for _ in range(len(fields)):
                streak += '-' * size_db + '|'
            write += streak[:-1] + '\n'
            database.seek(0, 0)
            database.write(write)
            database.flush()
            check = False
        else:
            print('БД уже инициализирована')

    #Вывод записей БД
    elif var == 3: 
        if file is None:
            print('Не выбран файл для инициализации БД')
            continue
        database.seek(0)
        row = database.readline()[:-1]
        if row == '': 
            print('В БД нет содержимого')
            continue
        while row:
            print(row)
            row = database.readline()[:-1]

    #Добавление записи в БД
    elif var == 4:
        if file is None:
            print('Не выбран файл для инициализации БД')
            continue
        while True:
            flag = True
            row = input('Введите содержимое записи через пробел: ').strip().split()
            if len(row) != len(fields):
                print('Количество элементов не совпадает. Повторите ввод')
                continue
            for i in range(len(row)):
                if fields[i][1] == 'int' and isDigit(row[i]) != True:
                    print('Ошибка. Тип данных {}-ого элемента не совпадает с типом данных поля. Повторите ввод'.format(i+1))
                    flag = False
                    break

            if flag == True:
                break
            continue
        write = ''
        for el in row:
            write += '{:^{}}|'.format(el, size_db)
        write = write[:-1] + '\n'
        database.seek(0,2)
        database.write(write)
        database.flush()
    
    #Поиск записей по одному полю
    elif var == 5:
        if file is None:
            print('Не выбран файл для инициализации БД')
            continue
        database.seek(0, 0)
        search1 = input('Введите название поля для поиска и шаблон имени через пробел: ').split()
        flag1 = False
        flag2 = False
        for i in range(len(fields)):
            if search1[0] == fields[i][0]:
                flag1 = True
                row = database.readline()[:-1]
                while row:
                    row_copy = row.replace(' ', '').split('|')
                    if row_copy[i] == search1[1]:
                        flag2 = True
                        print(row)
                    row = database.readline()[:-1]
                        
        if flag1 == False:
            print('Введенное название не совпадает ни с одним из столбцов')
        if flag2 == False:
            print('Не найдено ни одного совпадения')

    #Поиск записей по двум полям
    elif var == 6:
        if file is None:
            print('Не выбран файл для инициализации БД')
            continue
        database.seek(0)

        search1 = input('Введите первое название поля для поиска и шаблон имени через пробел: ').split()
        search2 = input('Введите второе название поля для поиска и шаблон имени через пробел: ').split()
        flag1 = False
        flag2 = False

        for i in range(len(fields) - 1):
            for j in range(i + 1, len(fields)):
                if search1[0] == fields[i][0] and search2[0] == fields[j][0]:
                    flag1 = True
                    row = database.readline()[:-1]
                    while row:
                        row_split = row.replace(' ', '').split('|')
                        if row_split[i] == search1[1] and row_split[j] == search2[1]:
                            flag2 = True
                            print(row)
                        row = database.readline()[:-1]
        if flag1 == False:
            print('Одно или несколько введенных названий не совпадают ни с одним из столбцов')
        if flag2 == False:
            print('Не найдено ни одного совпадения')
    print('')



    
