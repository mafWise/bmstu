# Вычисление значений функций при подстановки введенного аргумента и вывод таблицы с результатами.
# Построение одного из графиков функция и выполнение доп задания

import math as m
# Ввод значений
x0, xn = map(float, input(\
    'Введите значение первого и последнего аргумента через пробел: '\
    ).split())
step = float(input('Введите шаг: '))

diff = int((xn - x0) / step) + 1

x0_copy = x0
max_y, min_y = 0, 1000000
exp = 0.00001
ordinat = None
add_task = 0

# Вычисления значений функция и их вывод в таблицу
print('-' * 79 +\
      '\n|{:^25s}|{:^25s}|{:^25s}|\n'.format('x','y1', 'y2') +\
      '|' + '-' * 77 + '|')
for i in range(diff):
    if x0 > xn: break
    y1 = x0_copy**2 - m.sin(m.pi * x0_copy)
    y2 = 7.5*x0_copy**4 - 11*x0_copy**3 + 3.8*x0_copy**2 + 0.4*x0_copy - 0.98
    if y1 > 0: add_task += y1
    if y1 > 0 - exp and y1 < 0 + exp and y1 != 0: ordinat = int(y1) + 1
    now_y = y1
    if y1 > max_y: max_y = y1
    if y1 < min_y: min_y = y1
    print('|{:^25f}|{:^25f}|{:^25f}|'.format(x0_copy, y1, y2))
    x0_copy += step

print('-' * 79)
print('Сумма положительных значений: ', add_task)

# Построение масштабной линейки
size = 100
notchs = int(input('\nВведите количество засечек (4-8): '))
headline = ''
step_count = size // (notchs - 1)

gap = (max_y - min_y) / size
temp = min_y

for i in range(notchs - 1):
    headline += '{1:^{0}.6}'.format(size // (notchs - 1), str(temp))
    temp += step_count * gap
    
headline += '{1:^{0}.6}'.format(size // (notchs - 1), str(max_y))
print(' ' * 16 + headline.strip())

# Построение графика функции
gap = size / ( max_y - min_y)
if ordinat != None: ordinat = round(ordinat * gap)


for i in range(diff):
    if x0 > xn: break
    y = x0**2 - m.sin(m.pi * x0)
    if x0 > 0 - exp and x0 < 0 + exp:
        row = '-' * size
        print('{:^15f}'.format(x0) + row)
        x0 += step
        continue
    id_cell = abs(round(gap * y))
    if ordinat == None:
        if y > 0:
            row = ' ' * int(id_cell - 1) + '*' + ' ' * int(size - id_cell)
        else:
            row = ' ' * int(size - id_cell - 1) + '*' + ' ' * int(id_cell) 
    else:
        if y > 0:
            row = ' ' * (ordinat) + '|' + ' ' * id_cell  + '*' + ' ' * (size - id_cell)
        elif y < 0:
            row = ' ' * (ordinat - id_cell - 1) + '*' + ' ' * id_cell  + '|' + ' ' * (size - ordinat)  
    if id_cell >= size:
        row = ' ' * (size - 1) + '*'

    print('{:^15f}|'.format(x0) + row)
    x0 += step

