"""
Работа с файлами. Инициализация БД и хранение информации в бинарном виде
"""

import struct
database_check = False # Проверка на инициализацию базы данных

def error_output():
    if var == 1:
        print('Требуется подключение БД')
    elif var == 2:
         print('Запрос к БД выполнить не удалось')
        
# Функция для распаковки записи 
def bytes_unpack(obj):
    string = []
    for i in struct.unpack("32s 32s 32s i", obj):
        try:
            string.append(str(i.strip(b'\x00'), "UTF-8"))
        except:
            string.append(str(i))
    return string

#Доступные возможности программы
variants = (
    'Выбрать файл для работы',
    'Инициализировать базу данных',
    'Вывести содержимое базы данных',
    'Добавить запись в базу данных',
    'Удаление записи по номеру строчки',
    'Поиск по одному полю',
    'Поиск по двум полям',
)

size = 90

print('\nДоступные коды подпрограмм:\n')
print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
for i in range(len(variants)):
    print('|' + '{:^4}|'.format(i + 1) + '{0:^{1}}'.format(variants[i], size - 6) + '|')
    print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
print('Для вывода таблички введите "t"\n')

file_path = False
# Основное тело программы
print("""БД, инициализируемая в ходе данной программы, нацелена на 
хранение информации об автомобилях: марка авто, тип кузова, гос. номер и год выпуска\n""")

while True:

    # Ввод кода подпрограммы
    var = input("Введите код программы: ")
    #
    if var == '1':
        print('Если файл не существует, программа сама создаст его')
        file_path = input("Введите полный или относительный путь к файлу: ")
        
        print('')
        if file_path != '':
            base = open(file_path, mode = 'wb+')
            base.close()
        else:
            print('Ошибка')
        
        
    #
    elif var == '2':
        print('')
        if file_path != None:
            base = open(file_path, mode = 'wb')
            print('База данных успешно инициализирована')
            database_check = True
        # except:
        #     print('Что-то пошло не так')
        #     database_check = False
    #
    elif var == '3':
        if database_check:
            base = open(file_path, mode = 'rb')
            count = 100
            data = base.read(count)
            while data:
                print('     '.join(bytes_unpack(data)))
                data = base.read(count)
            
        else:
            error_output()
    #
    elif var == '4':
        print('')
        if database_check:
            base = open(file_path, mode = 'ab') # append new lines to the end
            while True:
                print('Введите марку авто, тип кузова, гос. номер и год выпуска через запятую или Enter чтобы выйти: ')
                query = input("Новая запись: ").split(',')
                
                if query == ['']:
                    break
                
                if len(query) != 4:
                    print('Запись должна содержать 4 поля. Повторите ввод')
                    continue
                    
                for i in range(len(query)):
                    query[i] = query[i].strip() # delete spaces
                    if query[i] == '' or query[i] == ' ': # replace empty fields with '-'
                        if i == 3:
                            query[i] = 0
                        else:
                            query[i] = '-'
                
                if not query[3].isdigit():
                        print("Поле с годом должно содержать цифру или быть пустым. Повторите ввод")
                        continue
                
                if len(query[0]) > 32 or len(query[1]) > 32 or len(query[2]) > 32:
                    print("Каждое поле строк должно быть короче 32 символа. Повтроите ввод")
                    continue
                
                packet = struct.pack("32s 32s 32s i", bytes(query[0], encoding='utf-8'), \
                    bytes(query[1], encoding='utf-8'),  bytes(query[2], encoding='utf-8'),\
                         int(query[3]))
                
                base.write(packet)
                base.flush() # pushing data to database from buffer
                print("Запись добавлена")
                    
        else:
            error_output()
    #
    elif var == '5':
        if database_check:
            base = open(file_path, mode = 'ab')
            size = base.tell()
            base = open(file_path, mode = 'r+b')
            key = input("Введите номер строки которую нужно удалить: ")
            
            error = False # catch errors in input data
            
            try:
                key = int(key)
            except:
                print("Неверно введен ключ")
                error = True
                continue
                
            if key > size / 100 or key <= 0:
                error = True
                print('Такого номера нет в БД')
                    
            if not error: # if query was correct
                count = 100
                position = key * count
                base.seek(position)
                data = base.read(count)
                while data:
                    base.seek(position)
                    data = base.read(count)
                    base.seek(position - count)
                    base.write(data)
                    
                    position += count
                base.truncate(size - 100)
            else:
                error_output(2)
                
        else:
            error_output(1)
        print('')       
    #          
    elif var == '6':
        print('')
        if database_check:
            base = open(file_path, mode = 'rb')
            key = input("Выберите поле поиска: Марка авто - 0, тип кузова - 1, гос. номер - 2, год выпуска - 3: ")
            value = input("Впишите значение поля: ")
            
            error = False # catch errors in input data
            
            if key in '0123':
                key = int(key)
                if key < 0 or key > 3:
                    print('Столбца с таким номером не существует')
                    error = True
            else:
                print("Неверно введен ключ :(")
                error = True
                    
            if not error: # if query was correct
                count = 100
                data = base.read(count)
                while data:
                    if bytes_unpack(data)[key].strip() == value.strip():
                        print("     ".join(bytes_unpack(data)))
                    data = base.read(count)
            else:
                error_output(2)
                
        else:
            error_output(1)
    #
    elif var == '7':
        print('')
        if database_check:
            base = open(file_path, mode = 'rb')
            key1 = input("Выберите поле поиска: Марка авто - 0, тип кузова - 1, гос. номер - 2, год выпуска - 3: ")
            value1 = input("Впишите значение этого поля: ")
            
            key2 = input("Выберите поле поиска: Марка авто - 0, тип кузова - 1, гос. номер - 2, год выпуска - 3: ")
            value2 = input("Впишите значение этого поля: ")
            
            error = False # catch errors in input data
            
            if key1 in '0123' and key2 in '0123':
                key1 = int(key1)
                key2 = int(key2)
                if (key1 < 0 or key1 > 3) and (key2 < 0 or key2 > 3):
                    print('Столбца с таким номером не существует')
                    error = True
            else:
                print("Неверно введен ключ :(")
                error = True
                    
            if not error: # if query was correct
                count = 100
                data = base.read(count)
                while data:
                    if bytes_unpack(data)[key1].strip() == value1.strip() and bytes_unpack(data)[key2].strip() == value2.strip():
                        print("     ".join(bytes_unpack(data)))
                    data = base.read(count)
            else:
                error_output(2)
                
        else:
            error_output(1)
    #
    elif var == "t":
        print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')
        for i in range(len(variants)):
            print('|' + '{:^4}|'.format(i + 1) + '{0:^{1}}'.format(variants[i], size - 6) + '|')
            print('|' + '-' * 4 + '|' + '-' * (size - 6) + '|')        
    #
    elif var == '0':
        if database_check:
            base.close() # closing file
        break

    else:
        print('')
        print("Введен некоректный пункт меню")

