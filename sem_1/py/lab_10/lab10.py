#Вычисление интеграла разными методами (трапеций, симпсона)

#Проверка на числовую значимость
def isDigit(t):
    if t == '': return False
    if t[0] == '-':
        t = t[1:]
    if t.find('.') != 0:
        t = t.replace('.', '')
    return t.isdigit()

#Проверка числа на числовую значимость
def digit_input(stroke):
    while True:
        n = input(stroke).strip()
        if isDigit(n) == True and float(n) >= 0:
            return float(n)
        print('Введенный символ не является числом. Повторите ввод')

#Функция-------------------------------------
def f(x):
    return 4*x

#Интеграл------------------------------------
def I(x_i, x_j):
    def F(x):
        return 2*x**2
    return F(x_j) - F(x_i)
 
#Главные вычисления
def main_calculation(x0, xn, quantity, method):
    S = 0
    x = x0
    dist_between = (xn - x0) / quantity
    if method == 'trapezoid':
        for i in range(quantity):
            S += ( f(x) + f(x + dist_between) ) / 2 * dist_between
            x += dist_between
    elif method == 'parabola':
        dist_between = dist_between / 2
        for i in range(quantity * 2):
            if i % 2 ==0: S += dist_between/3 * (f(x) + 4*f(x + dist_between) + f(x + 2*dist_between))
            x += dist_between
    return S


def reset():
    global S_trapezoid, S_parabola, currently_x
    S_trapezoid, S_parabola = 0, 0
    currently_x = x0
while True:
    print('\n\n')
    #Ввод
    print('Функция 4x')
    x0 = digit_input('Введите значение начала отрезка: ')
    xn = digit_input('Введите значение конец отрезка: ')
    N1 = int(digit_input('Введите первый вариант количества участков разбиения: '))
    N2 = int(digit_input('Введите второй вариант количества участков разбиения: '))
    quantities = (N1, N2)

    #Ввод вычислений в таблицу
    table = [
        
        [
            main_calculation(x0, xn, N1, 'trapezoid'),
            main_calculation(x0, xn, N1, 'parabola')
        ],
        
        [
            main_calculation(x0, xn, N2, 'trapezoid'),
            main_calculation(x0, xn, N2, 'parabola')
        ]
    ]


    size = 94

    #Вывод таблички
    print('\n|' + '-' * ((size - 4) // 3) + '|'  + '-' * ((size - 4) // 3) + '|' + '-' * ((size - 4) // 3) + '|')
    print('|' + ' ' * ((size-4) // 3) + '|' + '{1:^{0}}'.format((size-4) // 3, 'Количество участков: {}'.format(str(quantities[0]))) + '|' +\
        '{1:^{0}}'.format((size-4) // 3, 'Количество участков: {}'.format(str(quantities[1]))) + '|'  )
    print('|' + '-' * ((size - 4) // 3) + '|'  + '-' * ((size - 4) // 3) + '|' + '-' * ((size - 4) // 3) + '|')
    print('|' + '{1:^{0}}'.format((size - 4) // 3,'Метод трапеций') + '|' + '{1:^{0}f}'.format((size-4) // 3, table[0][0]) + '|' +\
        '{1:^{0}f}'.format((size-4) // 3, table[1][0]) + '|'  )
    print('|' + '-' * ((size - 4) // 3) + '|'  + '-' * ((size - 4) // 3) + '|' + '-' * ((size - 4) // 3) + '|')
    print('|' + '{1:^{0}}'.format((size - 4) // 3,'Метод парабол') + '|' + '{1:^{0}f}'.format((size-4) // 3, table[0][1]) + '|' +\
        '{1:^{0}f}'.format((size-4) // 3, table[1][1]) + '|'  )
    print('|' + '-' * ((size - 4) // 3) + '|'  + '-' * ((size - 4) // 3) + '|' + '-' * ((size - 4) // 3) + '|')
    print('Точное значение интеграла: {:f}\n'.format(I(x0, xn)))

    #Вывод пояснений
    eps = digit_input('Введите точность: ')
    for i in range(2):
        if table[i][1] == '-':
            continue
        most_approximate_value = table[i][0] if abs(I(x0, xn) - table[i][0]) < abs(I(x0, xn) - table[i][1]) else table[i][1]
        print('Для {} разбиений метод {} является наиболее точным'.format(\
            quantities[i], 'трапеций' if abs(I(x0, xn) - table[i][0]) < abs(I(x0, xn) - table[i][1]) else 'парабол')\
            )
        print('Абсолютная погрешность: {:f}, относительная погрешность {:f}'.format(abs(I(x0, xn) - most_approximate_value), most_approximate_value / abs(I(x0, xn))))
        N = 1
        value = 'trapezoid' if most_approximate_value != table[i][0] else 'parabola'
        while not (abs(main_calculation(x0, xn, N, value) - main_calculation(x0, xn, 2*N, value)) < eps):
            N += 1
        print('Количество участков разбиения для достижения точности {} равно {} при методе {}'.format(eps, N, 'трапеций' if value == 'trapezoid' else 'парабол'))
        print('Вычисленное значение интеграла с {} участком разделения равно {}'.format(N, main_calculation(x0, xn, N, value)))
        print('')
