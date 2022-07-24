
from random import randint
from time import perf_counter

def random_massive(range1):
    random = []
    while len(random) != len(range1):
        x = randint(0, len(range1) - 1)
        if random.count(x) == 0:
            random.append(x)
    for i in range(len(random)):
        random[i] = range1[random[i]]
    return random

def massive_input(stroke):
    while True:
        massive = list(map(str, input(stroke).strip().split()))
        if massive == []:
            print('Массив пуст. Повторите ввод')
            continue
        check = True
        for i in range(len(massive)):
            try: 
                float(massive[i])
            except: 
                print('{}-ый элемент в массиве не является числом. Повторите ввод'.format(i + 1)) 
                check = False
                break
        if check == True: return list(map(float, massive))

def gnome_sort_asc(massive):
    i = 0
    l = len(massive)
    t_start = perf_counter()
    while i < l:
        if i == 0 or massive[i - 1] <= massive[i]:
            i += 1
        else:
            lower = massive[i]
            massive[i] = massive[i-1]
            massive[i-1] = lower
            i -= 1
        
    return perf_counter() - t_start
def gnome_sort_desc(massive):
    i = 0
    l = len(massive)
    t_start = perf_counter()
    while i < l:
        if i == 0 or massive[i - 1] >= massive[i]:
            i += 1
        else:
            lower = massive[i]
            massive[i] = massive[i-1]
            massive[i-1] = lower
            i -= 1
    return perf_counter() - t_start

def gnome_sort_random(massive, random):
    i = 0
    j = 0
    l = len(massive)
    t_start = perf_counter()
    while i < l:
        if massive[i] != random[i]:
            while massive[i] != random[i]:
                if massive[j] != random[i]:
                    j += 1
                else:
                    lower = massive[j]
                    massive[j] = massive[j-1]
                    massive[j-1] = lower
                    j -= 1
        i += 1
    return perf_counter() - t_start
# range1 = massive_input('Введите элементы 1-ого массива через пробел: ')
range1 = [21,32,332,434,12]
random1 = random_massive(range1)
range2 = [123,76,2345,0,32]
# range2 = massive_input('Введите элементы 2-ого массива через пробел: ')
random2 = random_massive(range2)
# range3 = massive_input('Введите элементы 3-ого массива через пробел: ')
range3 = [123,435879,3652534,5345,2357568,5768]
random3 = random_massive(range3)
print(gnome_sort_asc(range1))
print(gnome_sort_desc(range1))
# print(range1)
# print(random)
size = 120

var=('Отсортированный по возрастанию список', 'Случайный список', 'Остортированный по убыванию список')
ranges=(range1, range2, range3)
results=[]
for i in ranges:
    results.append([gnome_sort_asc(i), gnome_sort_desc(i),gnome_sort_random(i, random_massive(i))])

print('\n|' + '-' * (size // 3) + '|'  + '-' * (size // 3) + '|' + '-' * (size // 3) + '|' + '-' * (size // 3) + '|')
print('|' + ' ' * (size // 3) + '|' + '{:^{}}'.format('Первый массив', size // 3) + '|' +\
    '{:^{}}'.format('Второй массив',size // 3) + '|'  +\
    '{:^{}}'.format('Третий массив',size // 3) + '|')
for i in range(3):

    print('|' + '-' * (size // 3) + '|'  + '-' * (size // 3) + '|' + '-' * (size // 3) + '|' + '-' * (size // 3) + '|')
    print('|' + '{1:^{0}}'.format(size // 3,var[i]) + '|' + '{1:^{0}g}'.format(size // 3, results[i][0]) + '|' +\
        '{1:^{0}g}'.format(size // 3, results[i][1]) + '|' + '{1:^{0}g}'.format(size // 3, results[i][2]) + '|')
print('|' + '-' * (size // 3) + '|'  + '-' * (size // 3) + '|' + '-' * (size // 3) + '|' + '-' * (size // 3) + '|')

